#!/usr/bin/env python3
"""
One-Click Vercel Deployment Helper
"""

import webbrowser
import time

def main():
    print("🚀 One-Click Vercel Deployment")
    print("=" * 40)
    print("I'll open the exact pages you need!")
    print()
    
    # Step 1: Open Vercel Dashboard
    print("📱 Step 1: Opening Vercel Dashboard...")
    webbrowser.open('https://vercel.com/dashboard')
    time.sleep(2)
    
    # Step 2: Open GitHub repository
    print("📱 Step 2: Opening your GitHub repository...")
    webbrowser.open('https://github.com/pranjaldesign/linkedin-post-agent')
    time.sleep(2)
    
    print()
    print("✅ Both pages are now open!")
    print()
    print("📋 Now follow these exact steps:")
    print()
    print("1. In the Vercel tab:")
    print("   - Sign in with GitHub")
    print("   - Click 'New Project'")
    print("   - Find 'linkedin-post-agent' and click it")
    print("   - Click 'Import'")
    print()
    print("2. Configure settings:")
    print("   - Framework Preset: Other")
    print("   - Root Directory: ./ (leave default)")
    print("   - Build Command: (leave empty)")
    print("   - Output Directory: public")
    print("   - Install Command: (leave empty)")
    print()
    print("3. Click 'Deploy' and wait 1-2 minutes!")
    print()
    print("🎉 Your app will be live at:")
    print("   https://linkedin-post-agent-[random].vercel.app")
    print()
    print("Need help? Check VERCEL_STEP_BY_STEP.md for detailed instructions!")

if __name__ == "__main__":
    main() 