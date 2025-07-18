# LinkedIn Post Agent - Web Interface

An AI-powered LinkedIn content creation and posting tool with a beautiful web interface. This agent can research topics, draft engaging LinkedIn posts, and automatically post them to your LinkedIn account.

## Features

- 🔍 **Web Research**: Automatically searches the web for relevant information on your topic
- ✍️ **AI-Powered Drafting**: Uses Google's Gemini AI to create engaging LinkedIn posts
- 🚀 **Smart LinkedIn Integration**: 
  - Checks if you're already logged into LinkedIn in your browser
  - Uses saved credentials if available
  - Prompts for manual login if needed
  - No need to store credentials if you prefer manual login
- 🌐 **Beautiful Web Interface**: Modern, responsive web UI for easy interaction
- 🔒 **Secure**: Optional credential storage with browser-based authentication

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Set Up Environment Variables

Create a `.env` file in the project root with your credentials:

```env
# LinkedIn credentials (optional - will use browser login if not provided)
LINKEDIN_EMAIL=your_linkedin_email@example.com
LINKEDIN_PASSWORD=your_linkedin_password

# Google Cloud settings
GOOGLE_GENAI_USE_VERTEXAI=TRUE
GOOGLE_CLOUD_PROJECT=your_project_id
GOOGLE_CLOUD_LOCATION=global
SECRET_KEY=your_secret_key_for_flask
```

**Note**: LinkedIn credentials are optional. The system will first check if you're already logged into LinkedIn in your browser. If not, it will either use saved credentials from the .env file or prompt you to log in manually.

### 3. Set Up Google Cloud Authentication

If you're using Google Cloud (recommended):

```bash
# Authenticate with Google Cloud
./google-cloud-sdk/bin/gcloud auth login
./google-cloud-sdk/bin/gcloud auth application-default login

# Set your project ID
./google-cloud-sdk/bin/gcloud config set project YOUR_PROJECT_ID

# Enable the Gemini API
./google-cloud-sdk/bin/gcloud services enable generativelanguage.googleapis.com
```

Alternatively, you can use a Google API key by setting `GOOGLE_API_KEY=your_api_key` in your `.env` file.

### 4. Install Playwright Browsers

```bash
playwright install chromium
```

### 5. Run the Web Interface

```bash
python run_web.py
```

The web interface will be available at: http://localhost:4000

## How to Use

### Step 1: Research
1. Enter a topic you want to post about
2. Click "Research Topic" to gather information from the web
3. Review the research results

### Step 2: Draft
1. The AI will generate a LinkedIn post based on the research
2. Edit the draft if needed
3. Click "Approve & Post" when satisfied

### Step 3: Post
1. Review the final post preview
2. Click "Post to LinkedIn" to publish
3. Complete any security checks in the browser window that opens

## Project Structure

```
linkedin-post-agent/
├── app.py                 # Flask web application
├── run_web.py            # Web interface runner
├── requirements.txt      # Python dependencies
├── templates/
│   └── index.html       # Web interface template
├── linkedin_poster/
│   ├── __init__.py
│   └── agent.py         # Main agent logic
└── .env                 # Environment variables (create this)
```

## API Endpoints

- `GET /` - Main web interface
- `POST /research` - Research a topic
- `POST /draft` - Generate a post draft
- `POST /post` - Post to LinkedIn

## Requirements

- Python 3.8+
- LinkedIn account
- Google API key for Gemini AI
- Modern web browser

## Security Notes

- Never commit your `.env` file to version control
- Use strong passwords for your LinkedIn account
- Consider using LinkedIn's 2FA for additional security
- The web interface runs locally by default

## Troubleshooting

### Common Issues

1. **Import Errors**: Make sure all dependencies are installed
   ```bash
   pip install -r requirements.txt
   ```

2. **Playwright Issues**: Install browsers manually
   ```bash
   playwright install chromium
   ```

3. **LinkedIn Login Issues**: 
   - Check your credentials in `.env`
   - Complete any security checks in the browser
   - Ensure 2FA is properly configured

4. **API Key Issues**:
   - Verify your Google API key is valid
   - Ensure Gemini API is enabled in your Google Cloud project

### Getting Help

If you encounter issues:

1. Check the console output for error messages
2. Verify all environment variables are set correctly
3. Ensure your LinkedIn account doesn't have login restrictions
4. Check that your Google API key has the necessary permissions

## Development

To contribute to this project:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer

This tool is for educational and personal use. Please comply with LinkedIn's Terms of Service and use responsibly. The authors are not responsible for any misuse of this tool. 