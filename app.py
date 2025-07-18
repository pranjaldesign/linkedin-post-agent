from flask import Flask, render_template, request, jsonify, session
import asyncio
import os
import google.generativeai as genai
from linkedin_poster.agent import root_agent, research_for_post, post_on_linkedin
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'your-secret-key-here')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/research', methods=['POST'])
def research():
    try:
        data = request.get_json()
        topic = data.get('topic', '').strip()
        
        if not topic:
            return jsonify({'error': 'Topic is required'}), 400
        
        # Run the async research function
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            research_result = loop.run_until_complete(research_for_post(topic))
            return jsonify({'research': research_result})
        finally:
            loop.close()
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/draft', methods=['POST'])
def draft():
    try:
        data = request.get_json()
        topic = data.get('topic', '').strip()
        research = data.get('research', '').strip()
        
        if not topic:
            return jsonify({'error': 'Topic is required'}), 400
        
        # Create a draft using a template-based approach
        # This provides a good starting point that users can edit
        
        # Extract key insights from research (simplified)
        research_summary = research[:500] + "..." if len(research) > 500 else research
        
        # Create a template-based draft
        draft_content = f"""🚀 Exciting developments in {topic}!

Based on recent research, I've discovered some fascinating insights that are worth sharing:

{research_summary}

💡 Key Takeaway: The landscape of {topic} is evolving rapidly, and staying informed is crucial for professionals in this space.

🤔 What's your experience with {topic}? Have you noticed similar trends in your industry?

#LinkedIn #ProfessionalDevelopment #{topic.replace(' ', '')} #Innovation #Technology"""
        
        return jsonify({'draft': draft_content})
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/post', methods=['POST'])
def post():
    try:
        data = request.get_json()
        post_content = data.get('content', '').strip()
        
        if not post_content:
            return jsonify({'error': 'Post content is required'}), 400
        
        # Run the async post function
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            result = loop.run_until_complete(post_on_linkedin(post_content))
            return jsonify({'result': result})
        finally:
            loop.close()
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 4000))
    app.run(debug=True, host='0.0.0.0', port=port) 