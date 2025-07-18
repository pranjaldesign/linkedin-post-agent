#!/usr/bin/env python3
"""
Final Render Deployment Script
"""

import webbrowser
import subprocess

def main():
    print("🚀 Deploying LinkedIn Post Agent to Render")
    print("=" * 50)
    print("✅ GitHub repository: https://github.com/pranjaldesign/linkedin-post-agent")
    print("✅ Code pushed successfully!")
    print("\n🌐 Now deploying to Render...")
    
    print("\n📋 Follow these steps:")
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
        print("\n🌐 Opening Render dashboard...")
    except:
        print("\nPlease manually open: https://render.com/dashboard")
    
    print("\n🎉 After deployment, your app will be available at:")
    print("https://linkedin-post-agent.onrender.com")
    
    print("\n📋 Quick Commands:")
    print("- View logs: Check Render dashboard")
    print("- Update app: git push origin main")
    print("- Check status: Render dashboard")
    
    print("\n🔧 Environment Variables Needed:")
    print("GOOGLE_API_KEY=your_google_api_key")
    print("LINKEDIN_EMAIL=your_linkedin_email")
    print("LINKEDIN_PASSWORD=your_linkedin_password")
    
    print("\n⏱️  Deployment typically takes 5-10 minutes")
    print("📊 You can monitor progress in the Render dashboard")

if __name__ == "__main__":
    main() 