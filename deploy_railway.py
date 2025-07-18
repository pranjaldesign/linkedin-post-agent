#!/usr/bin/env python3
"""
Railway Deployment Helper Script
"""

import os
import subprocess
import sys
from pathlib import Path

def check_git_repo():
    """Check if this is a git repository"""
    if not Path('.git').exists():
        print("❌ This is not a git repository.")
        print("Please initialize git and push to GitHub first:")
        print("  git init")
        print("  git add .")
        print("  git commit -m 'Initial commit'")
        print("  git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git")
        print("  git push -u origin main")
        return False
    return True

def check_railway_cli():
    """Check if Railway CLI is installed"""
    try:
        subprocess.run(['railway', '--version'], capture_output=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def install_railway_cli():
    """Install Railway CLI"""
    print("📦 Installing Railway CLI...")
    try:
        subprocess.run([sys.executable, '-m', 'pip', 'install', 'railway'], check=True)
        print("✅ Railway CLI installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install Railway CLI: {e}")
        return False

def deploy_to_railway():
    """Deploy to Railway"""
    print("🚀 Deploying to Railway...")
    
    # Check if logged in
    try:
        result = subprocess.run(['railway', 'whoami'], capture_output=True, text=True)
        if result.returncode != 0:
            print("🔐 Please log in to Railway first:")
            print("  railway login")
            return False
    except FileNotFoundError:
        print("❌ Railway CLI not found. Please install it first.")
        return False
    
    # Deploy
    try:
        subprocess.run(['railway', 'deploy'], check=True)
        print("✅ Deployment successful!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Deployment failed: {e}")
        return False

def main():
    print("🚀 Railway Deployment Helper")
    print("=" * 40)
    
    # Check git repository
    if not check_git_repo():
        return
    
    # Check Railway CLI
    if not check_railway_cli():
        if not install_railway_cli():
            return
    
    # Deploy
    if deploy_to_railway():
        print("\n🎉 Your LinkedIn Post Agent is now deployed!")
        print("📱 You can access it at the URL provided by Railway.")
        print("\n📋 Next steps:")
        print("1. Set up environment variables in Railway dashboard")
        print("2. Configure Google Cloud authentication")
        print("3. Test your deployed app")
    else:
        print("\n❌ Deployment failed. Please check the errors above.")

if __name__ == '__main__':
    main() 