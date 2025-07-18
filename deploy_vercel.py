#!/usr/bin/env python3
"""
Vercel Deployment Script for LinkedIn Post Agent
"""

import webbrowser
import subprocess
import os

def main():
    print("⚡ Deploying LinkedIn Post Agent to Vercel")
    print("=" * 50)
    
    # Check if files exist
    if not os.path.exists('vercel.json'):
        print("❌ vercel.json not found!")
        return
    
    if not os.path.exists('public/index.html'):
        print("❌ public/index.html not found!")
        return
    
    print("✅ Vercel files are ready!")
    print("✅ Static web app created")
    print("✅ Configuration files prepared")
    
    print("\n🌐 Opening Vercel Dashboard...")
    webbrowser.open('https://vercel.com/dashboard')
    
    print("\n📋 Follow these steps:")
    print("1. Sign in to Vercel (GitHub/Google)")
    print("2. Click 'New Project'")
    print("3. Import your GitHub repository:")
    print("   - Select 'linkedin-post-agent'")
    print("   - Vercel will auto-detect settings")
    print("4. Configure project:")
    print("   - Framework Preset: Other")
    print("   - Root Directory: ./")
    print("   - Build Command: (leave empty)")
    print("   - Output Directory: public")
    print("5. Click 'Deploy'")
    
    print("\n🚀 Your app will be deployed to:")
    print("   https://your-project-name.vercel.app")
    
    print("\n📁 Files being deployed:")
    print("   - public/index.html (your web app)")
    print("   - vercel.json (configuration)")
    
    print("\n✨ Features included:")
    print("   ✅ Modern, responsive UI")
    print("   ✅ Step-by-step workflow")
    print("   ✅ Demo mode for testing")
    print("   ✅ Mobile-friendly design")
    print("   ✅ Global CDN")
    print("   ✅ Automatic HTTPS")
    
    print("\n🔗 After deployment:")
    print("   - Share your Vercel URL")
    print("   - Add custom domain (optional)")
    print("   - Auto-deploy on git push")
    
    print("\n💡 For full functionality:")
    print("   - Deploy backend to Render/Heroku")
    print("   - Configure environment variables")
    print("   - Connect frontend to backend API")
    
    print("\n🎉 Ready to deploy! Follow the steps above.")

if __name__ == "__main__":
    main() 