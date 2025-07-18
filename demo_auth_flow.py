#!/usr/bin/env python3
"""
LinkedIn Post Agent - Authentication Flow Demo

This script demonstrates the new smart authentication flow:
1. First checks if user is already logged into LinkedIn
2. Uses saved credentials if available
3. Prompts for manual login if needed
"""

import asyncio
from linkedin_poster.agent import post_on_linkedin

async def demo_auth_flow():
    """Demonstrate the new authentication flow"""
    
    print("🔐 LinkedIn Authentication Flow Demo")
    print("=" * 50)
    
    print("\n📋 The new authentication system works as follows:")
    print("1. 🔍 Checks if you're already logged into LinkedIn in your browser")
    print("2. 🔑 Uses saved credentials from .env file if available")
    print("3. 🖱️  Prompts for manual login if no credentials are found")
    print("4. ✅ Proceeds with posting once authenticated")
    
    print("\n🚀 Starting authentication test...")
    
    # Test post content
    test_content = """🚀 Testing the new LinkedIn authentication flow!

This post was created using the LinkedIn Post Agent with smart authentication.

✅ No need to store credentials if you prefer manual login
✅ Uses browser session if already logged in
✅ Secure and user-friendly

#LinkedIn #Automation #Testing"""
    
    try:
        result = await post_on_linkedin(test_content)
        print(f"\n📤 Result: {result}")
    except Exception as e:
        print(f"\n❌ Error: {e}")
    
    print("\n" + "=" * 50)
    print("✨ Demo completed!")

if __name__ == "__main__":
    asyncio.run(demo_auth_flow()) 