#!/usr/bin/env python3
"""
Firebase Deployment Script for LinkedIn Post Agent
"""

import webbrowser
import subprocess
import os

def main():
    print("🔥 Deploying LinkedIn Post Agent to Firebase")
    print("=" * 50)
    
    # Check if files exist
    if not os.path.exists('firebase.json'):
        print("❌ firebase.json not found!")
        return
    
    if not os.path.exists('public/index.html'):
        print("❌ public/index.html not found!")
        return
    
    print("✅ Firebase files are ready!")
    print("✅ Static web app created")
    print("✅ Configuration files prepared")
    
    print("\n🌐 Opening Firebase Console...")
    webbrowser.open('https://console.firebase.google.com/')
    
    print("\n📋 Follow these steps:")
    print("1. Sign in to Google account")
    print("2. Click 'Create a project' or select existing")
    print("3. Enter project name: 'linkedin-post-agent'")
    print("4. Click 'Continue' (skip Google Analytics)")
    print("5. Click 'Create project'")
    print("6. Click 'Continue'")
    print("7. In the left sidebar, click 'Hosting'")
    print("8. Click 'Get started'")
    print("9. Choose 'Public directory': public")
    print("10. Click 'Next'")
    print("11. Click 'Deploy'")
    
    print("\n🚀 Your app will be deployed to:")
    print("   https://your-project-id.web.app")
    
    print("\n📁 Files to upload:")
    print("   - public/index.html (your web app)")
    print("   - firebase.json (configuration)")
    
    print("\n✨ Features included:")
    print("   ✅ Modern, responsive UI")
    print("   ✅ Step-by-step workflow")
    print("   ✅ Demo mode for testing")
    print("   ✅ Mobile-friendly design")
    
    print("\n🔗 After deployment:")
    print("   - Share your Firebase URL")
    print("   - Add custom domain (optional)")
    print("   - Connect GitHub for auto-deploy")
    
    print("\n💡 For full functionality:")
    print("   - Deploy backend to Render/Heroku")
    print("   - Configure environment variables")
    print("   - Connect frontend to backend API")
    
    print("\n🎉 Ready to deploy! Follow the steps above.")

if __name__ == "__main__":
    main() 