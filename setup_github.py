#!/usr/bin/env python3
"""
GitHub Setup and Render Deployment Script
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

def main():
    print("🚀 GitHub Setup and Render Deployment")
    print("=" * 50)
    
    # Check if we have a remote repository
    result = subprocess.run(['git', 'remote', '-v'], capture_output=True, text=True)
    
    if not result.stdout.strip():
        print("📦 Setting up GitHub repository...")
        print("\nPlease follow these steps:")
        print("1. Go to https://github.com/new")
        print("2. Create a new repository named 'linkedin-post-agent'")
        print("3. Make it PUBLIC (important for free deployment)")
        print("4. Don't initialize with README (we already have files)")
        print("5. Copy the repository URL")
        
        # Get repository URL from user
        repo_url = input("\nEnter your GitHub repository URL (e.g., https://github.com/username/linkedin-post-agent): ").strip()
        
        if not repo_url:
            print("❌ No repository URL provided. Exiting.")
            return
        
        # Add remote and push
        print(f"\n🔄 Adding remote repository: {repo_url}")
        run_command(f"git remote add origin {repo_url}", "Adding remote repository")
        run_command("git branch -M main", "Setting main branch")
        run_command("git push -u origin main", "Pushing to GitHub")
        
        print("\n✅ GitHub repository set up successfully!")
    else:
        print("✅ GitHub repository already configured")
    
    # Now deploy to Render
    print("\n🌐 Deploying to Render...")
    print("Please follow these steps:")
    print("1. Go to https://render.com/dashboard")
    print("2. Sign up/login (free)")
    print("3. Click 'New +' and select 'Blueprint'")
    print("4. Connect your GitHub account")
    print("5. Select the 'linkedin-post-agent' repository")
    print("6. Render will automatically detect render.yaml")
    print("7. Configure environment variables:")
    print("   - GOOGLE_API_KEY: your_google_api_key")
    print("   - LINKEDIN_EMAIL: your_linkedin_email")
    print("   - LINKEDIN_PASSWORD: your_linkedin_password")
    print("8. Click 'Apply' to deploy")
    
    # Open Render dashboard
    try:
        webbrowser.open('https://render.com/dashboard')
    except:
        print("Please manually open: https://render.com/dashboard")
    
    print("\n🎉 After deployment, your app will be available at:")
    print("https://linkedin-post-agent.onrender.com")
    
    print("\n📋 Quick Commands:")
    print("- View logs: Check Render dashboard")
    print("- Update app: git push origin main")
    print("- Check status: Render dashboard")

if __name__ == "__main__":
    main() 