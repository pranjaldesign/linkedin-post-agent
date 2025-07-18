import os
import json
import time
import asyncio
import httpx
from playwright.async_api import async_playwright
import google.generativeai as genai
from googlesearch import search
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from google.adk.agents import Agent
from google.genai.errors import ServerError

async def _get_content(url: str, client: httpx.AsyncClient) -> str:
    try:
        response = await client.get(url, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'lxml')
            paragraphs = [p.get_text() for p in soup.find_all('p')]
            print(f"  - Fetched content from {url}")
            return " ".join(paragraphs)
        return ""
    except Exception:
        return ""

async def _search_and_research(topic: str) -> str:
    """
    Performs a web search to gather information on the given topic.
    """
    print(f"🔎 Searching the web for: '{topic}'")
    
    try:
        results = list(search(topic, num_results=5))
    except Exception as e:
        print(f"An error occurred during search: {e}")
        return "Could not perform web search."
    
    if not results:
        return "No search results found."

    print(f"Found {len(results)} potential sources. Fetching content...")

    async with httpx.AsyncClient() as client:
        tasks = [_get_content(url, client) for url in results]
        content = await asyncio.gather(*tasks)

    content = [c for c in content if c]
    if not content:
        print("Could not fetch content from any source. Aborting.")
        return "No content found."

    return "\\n\\n---\\n\\n".join(content)

async def research_for_post(topic: str) -> str:
    """
    Researches a topic to gather information for drafting a LinkedIn post.
    This tool returns raw research material. The agent should use this material
    to draft the post itself.

    Args:
        topic (str): The topic to research.

    Returns:
        str: The raw research material.
    """
    print("✍️ Researching for LinkedIn post...")
    research = await _search_and_research(topic)
    return research

async def post_on_linkedin(post_content: str) -> str:
    """
    Posts content to LinkedIn, checking if user is already logged in first.
    """
    print("🤖 Automating LinkedIn post...")
    load_dotenv()
    
    async with async_playwright() as p:
        # Launch browser with persistent context to access saved credentials
        context = await p.chromium.launch_persistent_context(
            user_data_dir="./browser_data",
            headless=False,
            args=[
                '--no-first-run',
                '--no-default-browser-check'
            ]
        )
        page = await context.new_page()
        
        try:
            # First, try to go directly to LinkedIn feed to check if already logged in
            print("  - Checking if already logged into LinkedIn...")
            await page.goto("https://www.linkedin.com/feed/", timeout=30000)
            
            # Check if we're on the feed page (logged in) or redirected to login
            current_url = page.url
            
            if "login" in current_url or "signup" in current_url:
                print("  - Not logged in. Checking for saved credentials...")
                
                # Check if we have credentials in .env file
                email = os.environ.get("LINKEDIN_EMAIL")
                password = os.environ.get("LINKEDIN_PASSWORD")
                
                if email and password:
                    print("  - Using saved credentials from .env file...")
                    await page.fill('input#username', email)
                    await page.fill('input#password', password)
                    await page.click('button[type="submit"]')
                    
                    print("  - LinkedIn may ask for a security check. Please complete it in the browser window.")
                    # Wait for navigation to the feed page to ensure login is complete
                    try:
                        await page.wait_for_url("https://www.linkedin.com/feed/**", timeout=180000)
                        print("  - Login successful.")
                    except Exception as login_error:
                        return f"Login failed. Please check your credentials and complete any security checks. Error: {login_error}"
                else:
                    print("  - No saved credentials found. Please log in manually...")
                    return "Please log into LinkedIn in the browser window that opened. Once logged in, the post will be created automatically."
            else:
                print("  - Already logged into LinkedIn!")
            
            # Now create the post
            print("  - Creating a post...")
            # Navigate to the post creation page
            await page.goto("https://www.linkedin.com/feed/?shareActive=true")
            
            # Wait for the post editor to be ready
            post_editor_selector = "div.ql-editor"
            try:
                await page.wait_for_selector(post_editor_selector, timeout=30000)
            except Exception:
                # Try alternative selectors
                alternative_selectors = [
                    "div[data-placeholder='What do you want to talk about?']",
                    "div[role='textbox']",
                    "div[contenteditable='true']"
                ]
                
                editor_found = False
                for selector in alternative_selectors:
                    try:
                        await page.wait_for_selector(selector, timeout=5000)
                        post_editor_selector = selector
                        editor_found = True
                        break
                    except Exception:
                        continue
                
                if not editor_found:
                    return "Could not find the post editor. Please ensure you're logged into LinkedIn and try again."
            
            # Fill in the post content
            await page.locator(post_editor_selector).fill(post_content)
            await asyncio.sleep(1)
            
            # Click the post button
            post_button_selectors = [
                "button.share-actions__primary-action",
                "button[type='submit']",
                "button:has-text('Post')",
                "button:has-text('Share')"
            ]
            
            posted = False
            for selector in post_button_selectors:
                try:
                    await page.click(selector, timeout=5000)
                    posted = True
                    print("  - Post button clicked.")
                    break
                except Exception:
                    continue
            
            if not posted:
                return "Could not find the post button. Please check the browser window and post manually."
            
            # Wait for confirmation that the post was successful
            try:
                await page.wait_for_selector("text=Post successful", timeout=30000)
                print("  - Post published successfully!")
                return "Successfully posted on LinkedIn!"
            except Exception:
                # Check for other success indicators
                try:
                    await page.wait_for_selector("text=Your post was shared", timeout=10000)
                    print("  - Post published successfully!")
                    return "Successfully posted on LinkedIn!"
                except Exception:
                    # If we can't find success message, assume it worked if we're still on the page
                    await asyncio.sleep(3)
                    if "feed" in page.url:
                        print("  - Post appears to have been published successfully!")
                        return "Successfully posted on LinkedIn!"
                    else:
                        return "Post may have been published, but couldn't confirm. Please check your LinkedIn feed."
                        
        except Exception as e:
            error_message = f"An error occurred: {e}"
            print(f"An error occurred: {e}")
            try:
                screenshot_path = "linkedin_error.png"
                await page.screenshot(path=screenshot_path)
                print(f"  - Screenshot of the error page saved to {screenshot_path}")
                error_message += f". A screenshot has been saved to {screenshot_path}"
            except Exception as screenshot_error:
                print(f"Failed to take screenshot: {screenshot_error}")

            return error_message
        finally:
            await context.close()

root_agent = Agent(
    name="linkedin_poster",
    model="gemini-2.0-flash",
    description="An agent that can research a topic, draft a LinkedIn post, and post it to LinkedIn after user approval.",
    instruction="""You are an expert content creator. Your goal is to help users post on LinkedIn.
1. First, use the `research_for_post` tool to gather information on the user's topic.
2. Using the research material returned by the tool, draft a LinkedIn post. The post must be under 300 words, start with a hook, include an insight or opinion, and end with a question to encourage discussion.
3. Then, show the complete draft to the user for their review and ask for approval.
4. If they approve it, use the `post_on_linkedin` tool to post the drafted content on their behalf.""",
    tools=[research_for_post, post_on_linkedin],
) 