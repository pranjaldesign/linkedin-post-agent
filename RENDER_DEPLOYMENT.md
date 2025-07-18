# Render Deployment Guide

Render is a modern cloud platform that's perfect for Python applications. It offers a generous free tier and is very easy to use.

## Why Render?

- ✅ **Free Tier**: 750 hours/month (enough for 24/7 operation)
- ✅ **Python Native**: Excellent Python support
- ✅ **Easy Setup**: Simple deployment process
- ✅ **Auto-Deploy**: Deploys on every git push
- ✅ **Custom Domains**: Free custom domains
- ✅ **SSL Certificates**: Automatic HTTPS

## Prerequisites

1. **GitHub Account** (free)
2. **Render Account** (free at [render.com](https://render.com))
3. **Google API Key** (for Gemini AI)
4. **LinkedIn Credentials** (for posting)

## Quick Deployment Steps

### 1. Prepare Your Repository

```bash
# Make sure all changes are committed
git add .
git commit -m "Ready for deployment"

# Push to GitHub
git push origin main
```

### 2. Run the Deployment Script

```bash
python3 deploy_render.py
```

This will:
- Check your git repository status
- Open the Render dashboard
- Guide you through the setup process

### 3. Manual Deployment (Alternative)

If you prefer to deploy manually:

1. **Go to Render Dashboard**: https://render.com/dashboard
2. **Create New Web Service**:
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Select the repository with your LinkedIn Post Agent

3. **Configure the Service**:
   - **Name**: `linkedin-post-agent`
   - **Environment**: `Python`
   - **Build Command**: `pip install -r requirements.txt && playwright install chromium`
   - **Start Command**: `python app.py`
   - **Plan**: `Free`

4. **Add Environment Variables**:
   - `GOOGLE_API_KEY`: Your Google API key
   - `LINKEDIN_EMAIL`: Your LinkedIn email
   - `LINKEDIN_PASSWORD`: Your LinkedIn password
   - `SECRET_KEY`: (auto-generated)

5. **Deploy**: Click "Create Web Service"

## Using render.yaml (Recommended)

I've created a `render.yaml` file that automates the configuration:

1. Go to https://render.com/dashboard
2. Click "New +" → "Blueprint"
3. Connect your GitHub repository
4. Render will automatically detect `render.yaml`
5. Configure environment variables
6. Deploy!

## Environment Variables

Make sure to set these in Render:

```env
GOOGLE_API_KEY=your_google_api_key
LINKEDIN_EMAIL=your_linkedin_email
LINKEDIN_PASSWORD=your_linkedin_password
SECRET_KEY=auto_generated_by_render
```

## Post-Deployment

After successful deployment:

1. **Your app URL**: `https://your-app-name.onrender.com`
2. **Auto-deploy**: Every push to main branch triggers deployment
3. **Logs**: Available in Render dashboard
4. **Monitoring**: Built-in health checks

## Troubleshooting

### Common Issues

1. **Build Fails**
   - Check logs in Render dashboard
   - Verify all dependencies are in `requirements.txt`
   - Ensure Python version is compatible

2. **App Won't Start**
   - Check start command: `python app.py`
   - Verify environment variables are set
   - Check logs for error messages

3. **Playwright Issues**
   - Build command includes: `playwright install chromium`
   - Render supports headless browsers

4. **Environment Variables**
   - Make sure all required variables are set
   - Check for typos in variable names

### Getting Help

- Render Documentation: [docs.render.com](https://docs.render.com)
- Render Community: [community.render.com](https://community.render.com)
- Render Status: [status.render.com](https://status.render.com)

## Cost

Render Free Tier includes:
- **750 hours/month** (enough for 24/7 operation)
- **512 MB RAM**
- **Shared CPU**
- **Custom domains**
- **SSL certificates**

The LinkedIn Post Agent will easily fit within these limits.

## Security Notes

- Environment variables are encrypted in Render
- Your `.env` file is not deployed (excluded by `.gitignore`)
- Render provides automatic HTTPS
- Never commit sensitive credentials to your repository

## Next Steps

After deployment:

1. **Test your app**: Visit the provided URL
2. **Set up custom domain** (optional)
3. **Configure auto-deploy** (already enabled)
4. **Monitor usage** in Render dashboard

## Alternative Platforms

If Render doesn't work for you, I can also help with:
- **Railway**: Simple deployment, $5 free credit
- **Heroku**: Classic platform, free tier available
- **Google Cloud Run**: Google's serverless platform
- **Vercel**: Great for web apps, free tier

Just let me know if you'd like to try a different platform! 