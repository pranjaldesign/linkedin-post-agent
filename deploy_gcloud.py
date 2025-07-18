#!/usr/bin/env python3
"""
Google Cloud Run Deployment Helper Script
"""

import os
import subprocess
import sys
from pathlib import Path

def check_gcloud_auth():
    """Check if gcloud is authenticated"""
    try:
        result = subprocess.run(['./google-cloud-sdk/bin/gcloud', 'auth', 'list'], 
                              capture_output=True, text=True, check=True)
        if 'pranjal.designxvation@gmail.com' in result.stdout:
            print("✅ Google Cloud authenticated")
            return True
        else:
            print("❌ Not authenticated with Google Cloud")
            return False
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ Google Cloud CLI not found")
        return False

def get_project_id():
    """Get the current project ID"""
    try:
        result = subprocess.run(['./google-cloud-sdk/bin/gcloud', 'config', 'get-value', 'project'], 
                              capture_output=True, text=True, check=True)
        project_id = result.stdout.strip()
        print(f"📋 Using project: {project_id}")
        return project_id
    except subprocess.CalledProcessError:
        print("❌ Could not get project ID")
        return None

def enable_apis():
    """Enable required APIs"""
    print("🔧 Enabling required APIs...")
    apis = [
        'run.googleapis.com',
        'cloudbuild.googleapis.com',
        'containerregistry.googleapis.com',
        'generativelanguage.googleapis.com'
    ]
    
    for api in apis:
        try:
            subprocess.run(['./google-cloud-sdk/bin/gcloud', 'services', 'enable', api], 
                          check=True, capture_output=True)
            print(f"✅ Enabled {api}")
        except subprocess.CalledProcessError:
            print(f"⚠️  Could not enable {api} (may already be enabled)")

def build_and_deploy():
    """Build and deploy to Cloud Run"""
    project_id = "gen-lang-client-0801809398"  # Use the actual project ID
    
    service_name = "linkedin-post-agent"
    region = "us-central1"
    
    print(f"🚀 Building and deploying to Cloud Run...")
    print(f"   Service: {service_name}")
    print(f"   Region: {region}")
    print(f"   Project: {project_id}")
    
    try:
        # Build and deploy in one command
        cmd = [
            './google-cloud-sdk/bin/gcloud', 'run', 'deploy', service_name,
            '--source', '.',
            '--platform', 'managed',
            '--region', region,
            '--project', project_id,
            '--allow-unauthenticated',
            '--set-env-vars', f'GOOGLE_CLOUD_PROJECT={project_id}',
            '--set-env-vars', 'GOOGLE_CLOUD_LOCATION=global',
            '--set-env-vars', 'GOOGLE_GENAI_USE_VERTEXAI=TRUE'
        ]
        
        # Add LinkedIn credentials if available
        linkedin_email = os.environ.get('LINKEDIN_EMAIL')
        linkedin_password = os.environ.get('LINKEDIN_PASSWORD')
        
        if linkedin_email and linkedin_password:
            cmd.extend(['--set-env-vars', f'LINKEDIN_EMAIL={linkedin_email}'])
            cmd.extend(['--set-env-vars', f'LINKEDIN_PASSWORD={linkedin_password}'])
        
        subprocess.run(cmd, check=True)
        print("✅ Deployment successful!")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Deployment failed: {e}")
        return False

def get_service_url():
    """Get the service URL"""
    try:
        result = subprocess.run(['./google-cloud-sdk/bin/gcloud', 'run', 'services', 'describe', 
                               'linkedin-post-agent', '--region=us-central1', '--format=value(status.url)'], 
                              capture_output=True, text=True, check=True)
        url = result.stdout.strip()
        print(f"🌐 Your app is available at: {url}")
        return url
    except subprocess.CalledProcessError:
        print("❌ Could not get service URL")
        return None

def main():
    print("🚀 Google Cloud Run Deployment Helper")
    print("=" * 50)
    
    # Check authentication
    if not check_gcloud_auth():
        print("🔐 Please authenticate with Google Cloud:")
        print("  ./google-cloud-sdk/bin/gcloud auth login")
        print("  ./google-cloud-sdk/bin/gcloud auth application-default login")
        return
    
    # Enable APIs
    enable_apis()
    
    # Build and deploy
    if build_and_deploy():
        print("\n🎉 Your LinkedIn Post Agent is now deployed!")
        get_service_url()
        print("\n📋 Next steps:")
        print("1. Test your deployed app")
        print("2. Set up LinkedIn credentials if needed")
        print("3. Configure any additional environment variables")
    else:
        print("\n❌ Deployment failed. Please check the errors above.")

if __name__ == '__main__':
    main() 