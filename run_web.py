#!/usr/bin/env python3
"""
LinkedIn Post Agent Web Interface Runner
"""

import os
import sys
import subprocess
from pathlib import Path

def check_dependencies():
    """Check if all required dependencies are installed"""
    package_imports = {
        'flask': 'flask',
        'google-generativeai': 'google.generativeai',
        'playwright': 'playwright',
        'python-dotenv': 'dotenv',
        'beautifulsoup4': 'bs4',
        'requests': 'requests',
        'lxml': 'lxml',
        'httpx': 'httpx',
        'google-adk': 'google.adk',
        'googlesearch-python': 'googlesearch'
    }
    
    missing_packages = []
    for package, import_name in package_imports.items():
        try:
            __import__(import_name)
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        print("❌ Missing dependencies:")
        for package in missing_packages:
            print(f"   - {package}")
        print("\nPlease install missing packages with:")
        print(f"pip install {' '.join(missing_packages)}")
        return False
    
    print("✅ All dependencies are installed")
    return True

def check_env_file():
    """Check if .env file exists with required variables"""
    env_file = Path('.env')
    if not env_file.exists():
        print("❌ .env file not found")
        print("Please create a .env file with the following variables:")
        print("LINKEDIN_EMAIL=your_linkedin_email")
        print("LINKEDIN_PASSWORD=your_linkedin_password")
        print("GOOGLE_API_KEY=your_google_api_key")
        return False
    
    print("✅ .env file found")
    return True

def install_playwright_browsers():
    """Install Playwright browsers if not already installed"""
    try:
        import playwright
        print("🔧 Installing Playwright browsers...")
        subprocess.run([sys.executable, '-m', 'playwright', 'install', 'chromium'], 
                      check=True, capture_output=True)
        print("✅ Playwright browsers installed")
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install Playwright browsers: {e}")
        return False
    except Exception as e:
        print(f"❌ Error installing Playwright browsers: {e}")
        return False
    
    return True

def main():
    print("🚀 Starting LinkedIn Post Agent Web Interface")
    print("=" * 50)
    
    # Check dependencies
    if not check_dependencies():
        sys.exit(1)
    
    # Check environment file
    if not check_env_file():
        sys.exit(1)
    
    # Install Playwright browsers
    if not install_playwright_browsers():
        print("⚠️  Continuing without Playwright browsers (may cause issues)")
    
    print("\n🌐 Starting web server...")
    print("The web interface will be available at: http://localhost:4000")
    print("Press Ctrl+C to stop the server")
    print("=" * 50)
    
    # Run the Flask app
    try:
        from app import app
        app.run(debug=True, host='0.0.0.0', port=4000)
    except KeyboardInterrupt:
        print("\n👋 Server stopped by user")
    except Exception as e:
        print(f"❌ Error starting server: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main() 