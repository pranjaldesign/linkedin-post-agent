# LinkedIn Post Agent - Deployment Guide

This guide will help you deploy your LinkedIn Post Agent to various free hosting platforms.

## 🚀 Quick Deploy Options

### Option 1: Railway (Recommended - Free Tier)

1. **Sign up for Railway**:
   - Go to [railway.app](https://railway.app)
   - Sign up with your GitHub account

2. **Deploy from GitHub**:
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your LinkedIn Post Agent repository
   - Railway will automatically detect the Python app

3. **Set Environment Variables**:
   - Go to your project settings
   - Add the following environment variables:
   ```
   LINKEDIN_EMAIL=your_linkedin_email@example.com
   LINKEDIN_PASSWORD=your_linkedin_password
   GOOGLE_GENAI_USE_VERTEXAI=TRUE
   GOOGLE_CLOUD_PROJECT=your_project_id
   GOOGLE_CLOUD_LOCATION=global
   SECRET_KEY=your_secret_key_here
   ```

4. **Deploy**:
   - Railway will automatically build and deploy your app
   - You'll get a URL like: `https://your-app-name.railway.app`

### Option 2: Render (Free Tier)

1. **Sign up for Render**:
   - Go to [render.com](https://render.com)
   - Sign up with your GitHub account

2. **Create New Web Service**:
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Choose the repository

3. **Configure the service**:
   - **Name**: `linkedin-post-agent`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt && playwright install chromium`
   - **Start Command**: `gunicorn app:app --bind 0.0.0.0:$PORT`

4. **Set Environment Variables**:
   - Add the same environment variables as above

5. **Deploy**:
   - Click "Create Web Service"
   - Render will build and deploy your app

### Option 3: Google Cloud Run (Free Tier)

1. **Install Google Cloud CLI**:
   ```bash
   # Already installed in your project
   ./google-cloud-sdk/bin/gcloud auth login
   ```

2. **Build and Deploy**:
   ```bash
   # Build the container
   docker build -t linkedin-post-agent .
   
   # Deploy to Cloud Run
   ./google-cloud-sdk/bin/gcloud run deploy linkedin-post-agent \
     --image gcr.io/YOUR_PROJECT_ID/linkedin-post-agent \
     --platform managed \
     --region us-central1 \
     --allow-unauthenticated \
     --set-env-vars="LINKEDIN_EMAIL=your_email,LINKEDIN_PASSWORD=your_password"
   ```

### Option 4: Heroku (Free Tier Discontinued)

Note: Heroku no longer offers a free tier, but you can use it with a paid plan.

1. **Install Heroku CLI**:
   ```bash
   # Install from https://devcenter.heroku.com/articles/heroku-cli
   ```

2. **Deploy**:
   ```bash
   heroku create your-app-name
   heroku config:set LINKEDIN_EMAIL=your_email
   heroku config:set LINKEDIN_PASSWORD=your_password
   git push heroku main
   ```

## 🔧 Environment Variables

Set these environment variables in your deployment platform:

```env
# LinkedIn credentials (optional)
LINKEDIN_EMAIL=your_linkedin_email@example.com
LINKEDIN_PASSWORD=your_linkedin_password

# Google Cloud settings
GOOGLE_GENAI_USE_VERTEXAI=TRUE
GOOGLE_CLOUD_PROJECT=your_project_id
GOOGLE_CLOUD_LOCATION=global

# Flask settings
SECRET_KEY=your_secret_key_here

# Platform settings
PORT=8080
```

## 🌐 Access Your Deployed App

Once deployed, you can access your LinkedIn Post Agent at:
- **Railway**: `https://your-app-name.railway.app`
- **Render**: `https://your-app-name.onrender.com`
- **Cloud Run**: `https://your-app-name-xxxxx-uc.a.run.app`

## 🔒 Security Notes

1. **Environment Variables**: Never commit sensitive data to your repository
2. **LinkedIn Credentials**: Consider using manual login instead of storing credentials
3. **Google Cloud**: Ensure your project has proper IAM permissions
4. **HTTPS**: All platforms provide HTTPS by default

## 🐛 Troubleshooting

### Common Issues:

1. **Playwright Installation**:
   - Ensure the platform supports browser installation
   - Some platforms may require additional system dependencies

2. **Google Cloud Authentication**:
   - Set up Application Default Credentials
   - Ensure the Gemini API is enabled

3. **LinkedIn Authentication**:
   - The app will prompt for manual login if credentials aren't stored
   - Browser automation may not work on all platforms

### Debug Commands:

```bash
# Check logs
railway logs
# or
heroku logs --tail

# Check environment variables
railway variables
# or
heroku config
```

## 📱 Using Your Deployed App

1. **Open the URL** in your browser
2. **Enter a topic** to research
3. **Review the AI-generated draft**
4. **Edit if needed**
5. **Post to LinkedIn** (will open browser for authentication)

## 🎉 Success!

Your LinkedIn Post Agent is now deployed and accessible from anywhere in the world! 