# Railway Deployment Guide

Railway is a simple and powerful platform for deploying Python applications. It offers a generous free tier and is perfect for this LinkedIn Post Agent.

## Prerequisites

1. **Node.js and npm** (for Railway CLI)
2. **Git** (for version control)
3. **Railway account** (free at [railway.app](https://railway.app))

## Quick Deployment Steps

### 1. Install Railway CLI

```bash
npm install -g @railway/cli
```

### 2. Run the Deployment Script

```bash
python3 deploy_railway_simple.py
```

The script will:
- Check if Railway CLI is installed
- Verify git repository status
- Log you into Railway
- Initialize the project
- Set environment variables from your `.env` file
- Deploy your application

### 3. Manual Deployment (Alternative)

If you prefer to deploy manually:

```bash
# Login to Railway
railway login

# Initialize project
railway init

# Set environment variables (if you have a .env file)
railway variables set GOOGLE_API_KEY="your_api_key"
railway variables set LINKEDIN_EMAIL="your_email"
railway variables set LINKEDIN_PASSWORD="your_password"

# Deploy
railway up
```

## Environment Variables

Make sure your `.env` file contains:

```env
GOOGLE_API_KEY=your_google_api_key
LINKEDIN_EMAIL=your_linkedin_email
LINKEDIN_PASSWORD=your_linkedin_password
```

## Post-Deployment

After successful deployment:

1. **Get your app URL**: `railway domain`
2. **View logs**: `railway logs`
3. **Open app**: `railway open`
4. **Check status**: `railway status`

## Troubleshooting

### Common Issues

1. **Railway CLI not found**
   - Install with: `npm install -g @railway/cli`

2. **Authentication issues**
   - Run: `railway logout` then `railway login`

3. **Environment variables not set**
   - Check your `.env` file exists
   - Set manually: `railway variables set KEY=value`

4. **Deployment fails**
   - Check logs: `railway logs`
   - Verify all dependencies are in `requirements.txt`

### Getting Help

- Railway Documentation: [docs.railway.app](https://docs.railway.app)
- Railway Discord: [discord.gg/railway](https://discord.gg/railway)

## Cost

Railway offers:
- **Free tier**: $5 credit monthly
- **Pro tier**: Pay-as-you-go
- **Team tier**: Collaborative features

The LinkedIn Post Agent should easily fit within the free tier limits.

## Security Notes

- Your `.env` file is automatically excluded from git
- Environment variables are encrypted in Railway
- Never commit sensitive credentials to your repository 