#!/usr/bin/env python3
"""
Simple Render Deployment Script for LinkedIn Post Agent
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

def check_git_status():
    """Check git repository status"""
    if not os.path.exists('.git'):
        print("❌ Not in a git repository!")
        print("Please run 'git init' and 'git add .' first.")
        return False
    
    result = subprocess.run(['git', 'status', '--porcelain'], capture_output=True, text=True)
    if result.stdout.strip():
        print("⚠️  You have uncommitted changes!")
        print("Please commit your changes before deploying:")
        print("git add .")
        print("git commit -m 'Your commit message'")
        return False
    
    return True

def main():
    print("🚀 Render Deployment for LinkedIn Post Agent")
    print("=" * 50)
    
    # Check git status
    if not check_git_status():
        return
    
    print("✅ All checks passed!")
    
    # Check if we have a GitHub repository
    result = subprocess.run(['git', 'remote', '-v'], capture_output=True, text=True)
    if not result.stdout.strip():
        print("\n📦 Setting up GitHub repository...")
        print("Please follow these steps:")
        print("1. Create a new repository on GitHub")
        print("2. Run these commands:")
        print("   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git")
        print("   git branch -M main")
        print("   git push -u origin main")
        print("\nAfter setting up GitHub, run this script again.")
        return
    
    print("\n🌐 Opening Render dashboard...")
    print("Please follow these steps:")
    print("1. Sign up/login to Render at https://render.com")
    print("2. Click 'New +' and select 'Web Service'")
    print("3. Connect your GitHub repository")
    print("4. Configure the service:")
    print("   - Name: linkedin-post-agent")
    print("   - Environment: Python")
    print("   - Build Command: pip install -r requirements.txt && playwright install chromium")
    print("   - Start Command: python app.py")
    print("5. Add environment variables:")
    print("   - GOOGLE_API_KEY: your_google_api_key")
    print("   - LINKEDIN_EMAIL: your_linkedin_email")
    print("   - LINKEDIN_PASSWORD: your_linkedin_password")
    print("6. Click 'Create Web Service'")
    
    # Open Render dashboard
    try:
        webbrowser.open('https://render.com/dashboard')
    except:
        print("Please manually open: https://render.com/dashboard")
    
    print("\n📋 Alternative: Use render.yaml")
    print("If you prefer, you can use the render.yaml file I created:")
    print("1. Go to https://render.com/dashboard")
    print("2. Click 'New +' and select 'Blueprint'")
    print("3. Connect your GitHub repository")
    print("4. Render will automatically detect render.yaml")
    print("5. Configure environment variables")
    print("6. Deploy!")
    
    print("\n🎉 After deployment, your app will be available at:")
    print("https://your-app-name.onrender.com")

if __name__ == "__main__":
    main() 