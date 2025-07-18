# Full Stack Deployment Guide

This guide will help you deploy both the frontend and backend to make your LinkedIn Post Agent fully functional.

## 🎯 **Current Status**

✅ **Frontend**: Deployed to Vercel (beautiful UI)  
❌ **Backend**: Not deployed (API endpoints don't work)  
❌ **Environment Variables**: Not configured  

## 🚀 **Step 1: Deploy Backend to Render**

### 1.1 Go to Render Dashboard
1. Open: https://render.com/dashboard
2. Sign up/login with GitHub
3. Click "New +" → "Blueprint"

### 1.2 Connect GitHub Repository
1. Connect your GitHub account
2. Select `linkedin-post-agent` repository
3. Render will auto-detect `render.yaml`
4. Click "Connect Repository"

### 1.3 Configure Environment Variables
Add these environment variables in Render:

```env
GOOGLE_API_KEY=your_google_api_key_here
LINKEDIN_EMAIL=your_linkedin_email@example.com
LINKEDIN_PASSWORD=your_linkedin_password
SECRET_KEY=any_random_string_for_security
```

### 1.4 Deploy
1. Click "Apply"
2. Wait 5-10 minutes for deployment
3. Your backend will be live at: `https://your-app-name.onrender.com`

## 🔗 **Step 2: Connect Frontend to Backend**

### 2.1 Update Frontend API URL
1. Go to your Vercel dashboard
2. Find your deployed project
3. Go to "Settings" → "Environment Variables"
4. Add: `BACKEND_URL=https://your-app-name.onrender.com`

### 2.2 Update Code (Alternative)
Or manually update `public/index.html`:
```javascript
const BACKEND_URL = 'https://your-app-name.onrender.com';
```

### 2.3 Redeploy Frontend
1. Push changes to GitHub
2. Vercel will auto-deploy
3. Your frontend will now connect to backend

## 🔧 **Step 3: Configure Environment Variables**

### 3.1 Get Google API Key
1. Go to: https://makersuite.google.com/app/apikey
2. Create a new API key
3. Copy the key

### 3.2 LinkedIn Credentials
Use your LinkedIn email and password (or create a test account)

### 3.3 Add to Render
In your Render app settings, add:
- `GOOGLE_API_KEY`: Your Google API key
- `LINKEDIN_EMAIL`: Your LinkedIn email
- `LINKEDIN_PASSWORD`: Your LinkedIn password

## ✅ **Step 4: Test Full Functionality**

### 4.1 Test Research
1. Go to your Vercel app
2. Enter a topic (e.g., "AI in design")
3. Click "Research Topic"
4. Should show real research results

### 4.2 Test Draft Generation
1. Enter a topic
2. Click "Generate Draft"
3. Should create a LinkedIn post draft

### 4.3 Test LinkedIn Posting
1. Enter post content
2. Click "Post to LinkedIn"
3. Should open browser and post to LinkedIn

## 🎉 **Success!**

Your LinkedIn Post Agent is now fully functional:
- ✅ **Frontend**: Beautiful UI on Vercel
- ✅ **Backend**: Python API on Render
- ✅ **AI Integration**: Google Gemini API
- ✅ **LinkedIn Automation**: Playwright browser automation

## 🔗 **Your URLs**

- **Frontend**: `https://your-project-name.vercel.app`
- **Backend**: `https://your-app-name.onrender.com`

## 🛠️ **Troubleshooting**

### Backend Not Working
1. Check Render logs for errors
2. Verify environment variables
3. Ensure `render.yaml` is correct

### Frontend Not Connecting
1. Check `BACKEND_URL` is correct
2. Verify CORS settings
3. Test backend URL directly

### LinkedIn Issues
1. Check credentials are correct
2. Ensure 2FA is disabled (for automation)
3. Try manual login first

## 📞 **Need Help?**

- **Render Support**: https://render.com/docs/help
- **Vercel Support**: https://vercel.com/support
- **Google AI**: https://ai.google.dev/

---

**Ready to deploy? Follow the steps above!** 🚀 