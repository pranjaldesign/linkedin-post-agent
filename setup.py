#!/usr/bin/env python3
"""
LinkedIn Post Agent Setup Script
"""

import os
import secrets
import subprocess
import sys
from pathlib import Path

def create_env_file():
    """Create .env file with template values"""
    env_file = Path('.env')
    
    if env_file.exists():
        print("⚠️  .env file already exists. Skipping creation.")
        return True
    
    print("📝 Creating .env file...")
    
    # Generate a random secret key
    secret_key = secrets.token_hex(32)
    
    env_content = f"""# LinkedIn Post Agent Environment Variables
# Fill in your actual values below

# LinkedIn Credentials
LINKEDIN_EMAIL=your_linkedin_email@example.com
LINKEDIN_PASSWORD=your_linkedin_password

# Google API Key for Gemini AI
GOOGLE_API_KEY=your_google_api_key_here

# Flask Secret Key (auto-generated)
SECRET_KEY={secret_key}

# Optional: Custom port for the web interface
# PORT=5000
"""
    
    try:
        with open(env_file, 'w') as f:
            f.write(env_content)
        print("✅ .env file created successfully!")
        print("📋 Please edit .env file with your actual credentials:")
        print("   - LINKEDIN_EMAIL: Your LinkedIn email")
        print("   - LINKEDIN_PASSWORD: Your LinkedIn password")
        print("   - GOOGLE_API_KEY: Your Google API key for Gemini AI")
        return True
    except Exception as e:
        print(f"❌ Failed to create .env file: {e}")
        return False

def install_dependencies():
    """Install Python dependencies"""
    print("📦 Installing Python dependencies...")
    
    try:
        subprocess.run([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'], 
                      check=True, capture_output=True)
        print("✅ Dependencies installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install dependencies: {e}")
        return False

def install_playwright_browsers():
    """Install Playwright browsers"""
    print("🔧 Installing Playwright browsers...")
    
    try:
        subprocess.run([sys.executable, '-m', 'playwright', 'install', 'chromium'], 
                      check=True, capture_output=True)
        print("✅ Playwright browsers installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install Playwright browsers: {e}")
        return False

def check_google_api_setup():
    """Provide instructions for Google API setup"""
    print("\n🔑 Google API Setup Instructions:")
    print("1. Go to https://console.cloud.google.com/")
    print("2. Create a new project or select an existing one")
    print("3. Enable the Gemini API:")
    print("   - Go to APIs & Services > Library")
    print("   - Search for 'Gemini API' and enable it")
    print("4. Create an API key:")
    print("   - Go to APIs & Services > Credentials")
    print("   - Click 'Create Credentials' > 'API Key'")
    print("5. Copy the API key and add it to your .env file")
    print("6. (Optional) Restrict the API key to Gemini API only")

def main():
    print("🚀 LinkedIn Post Agent Setup")
    print("=" * 40)
    
    # Install dependencies
    if not install_dependencies():
        print("❌ Setup failed at dependency installation")
        sys.exit(1)
    
    # Install Playwright browsers
    if not install_playwright_browsers():
        print("⚠️  Playwright browser installation failed, but continuing...")
    
    # Create .env file
    if not create_env_file():
        print("❌ Setup failed at .env file creation")
        sys.exit(1)
    
    # Show Google API setup instructions
    check_google_api_setup()
    
    print("\n" + "=" * 40)
    print("✅ Setup completed successfully!")
    print("\n📋 Next steps:")
    print("1. Edit the .env file with your actual credentials")
    print("2. Get a Google API key for Gemini AI")
    print("3. Run the web interface:")
    print("   python run_web.py")
    print("\n🌐 The web interface will be available at: http://localhost:4000")

if __name__ == '__main__':
    main() 