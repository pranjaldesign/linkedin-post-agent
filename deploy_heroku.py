#!/usr/bin/env python3
"""
Simple Heroku Deployment Script for LinkedIn Post Agent
"""

import os
import subprocess
import sys
import webbrowser

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"\n🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e}")
        print(f"Error output: {e.stderr}")
        return None

def check_heroku_cli():
    """Check if Heroku CLI is installed"""
    try:
        result = subprocess.run(['heroku', '--version'], capture_output=True, text=True)
        return True
    except FileNotFoundError:
        return False

def main():
    print("🚀 Heroku Deployment for LinkedIn Post Agent")
    print("=" * 50)
    
    # Check if Heroku CLI is installed
    if not check_heroku_cli():
        print("❌ Heroku CLI not found!")
        print("\n📦 Installing Heroku CLI...")
        print("Please run the following command:")
        print("brew tap heroku/brew && brew install heroku")
        print("\nAfter installation, run this script again.")
        return
    
    # Check if we're in a git repository
    if not os.path.exists('.git'):
        print("❌ Not in a git repository!")
        print("Please run 'git init' and 'git add .' first.")
        return
    
    # Check if we have uncommitted changes
    result = subprocess.run(['git', 'status', '--porcelain'], capture_output=True, text=True)
    if result.stdout.strip():
        print("⚠️  You have uncommitted changes!")
        print("Please commit your changes before deploying:")
        print("git add .")
        print("git commit -m 'Your commit message'")
        return
    
    print("✅ All checks passed!")
    
    # Login to Heroku
    print("\n🔐 Logging into Heroku...")
    print("Please follow the browser authentication...")
    run_command("heroku login", "Heroku login")
    
    # Create Heroku app
    print("\n🏗️  Creating Heroku app...")
    app_name = input("Enter a unique app name (or press Enter for auto-generated): ").strip()
    
    if app_name:
        create_command = f"heroku create {app_name}"
    else:
        create_command = "heroku create"
    
    result = run_command(create_command, "Heroku app creation")
    
    if not result:
        return
    
    # Set buildpacks
    print("\n🔧 Setting up buildpacks...")
    run_command("heroku buildpacks:add heroku/python", "Adding Python buildpack")
    run_command("heroku buildpacks:add https://github.com/heroku/heroku-buildpack-google-chrome", "Adding Chrome buildpack")
    
    # Set environment variables
    print("\n🔧 Setting up environment variables...")
    
    # Check if .env file exists
    if os.path.exists('.env'):
        print("📄 Found .env file, setting environment variables...")
        with open('.env', 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    run_command(f'heroku config:set {key}="{value}"', f"Setting {key}")
    
    # Deploy to Heroku
    print("\n🚀 Deploying to Heroku...")
    result = run_command("git push heroku main", "Heroku deployment")
    
    if result:
        print("\n🎉 Deployment completed successfully!")
        print("\n📋 Next steps:")
        print("1. Your app will be available at the URL shown above")
        print("2. You can view logs with: heroku logs --tail")
        print("3. You can open the app with: heroku open")
        print("4. You can check status with: heroku ps")
        
        # Get the app URL
        url_result = run_command("heroku info -s | grep web_url", "Getting app URL")
        if url_result:
            print(f"\n🌐 Your app is available at: {url_result.strip()}")
    else:
        print("\n❌ Deployment failed!")
        print("Please check the error messages above and try again.")

if __name__ == "__main__":
    main() 