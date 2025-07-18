#!/usr/bin/env python3
"""
Simple Railway Deployment Script for LinkedIn Post Agent
"""

import os
import subprocess
import sys

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

def check_railway_cli():
    """Check if Railway CLI is installed"""
    try:
        result = subprocess.run(['railway', '--version'], capture_output=True, text=True)
        return True
    except FileNotFoundError:
        return False

def main():
    print("🚀 Railway Deployment for LinkedIn Post Agent")
    print("=" * 50)
    
    # Check if Railway CLI is installed
    if not check_railway_cli():
        print("❌ Railway CLI not found!")
        print("\n📦 Installing Railway CLI...")
        print("Please run the following command:")
        print("npm install -g @railway/cli")
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
    
    # Login to Railway
    print("\n🔐 Logging into Railway...")
    print("Please follow the browser authentication...")
    run_command("railway login", "Railway login")
    
    # Initialize Railway project
    print("\n🏗️  Initializing Railway project...")
    run_command("railway init", "Railway project initialization")
    
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
                    run_command(f'railway variables set {key}="{value}"', f"Setting {key}")
    
    # Deploy to Railway
    print("\n🚀 Deploying to Railway...")
    result = run_command("railway up", "Railway deployment")
    
    if result:
        print("\n🎉 Deployment completed successfully!")
        print("\n📋 Next steps:")
        print("1. Your app will be available at the URL shown above")
        print("2. You can view logs with: railway logs")
        print("3. You can open the app with: railway open")
        print("4. You can check status with: railway status")
        
        # Get the deployment URL
        url_result = run_command("railway domain", "Getting deployment URL")
        if url_result:
            print(f"\n🌐 Your app is available at: {url_result.strip()}")
    else:
        print("\n❌ Deployment failed!")
        print("Please check the error messages above and try again.")

if __name__ == "__main__":
    main() 