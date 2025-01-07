from flask import Flask, jsonify
from dendrite_sdk import AsyncDendrite
from dendrite_sdk.remote import BrowserbaseConfig
import os

app = Flask(__name__)

@app.route('/health')
async def health_check():
    return jsonify({ 'status': 'healthy' }), 200

@app.route('/')
async def run_dendrite_auth():
    try:
        browser = AsyncDendrite(auth=["linkedin.com"], dendrite_api_key=os.getenv("DENDRITE_API_KEY"), playwright_options={ "headless": True})

        await browser.goto(
            "https://linkedin.com",
            expected_page="You should be logged in with the linkedin feed visible",
        )
        desc = await browser.ask("Get the latest post in the feed and profile views.")
        print("First post description: ", desc)

        await browser.close()
        
        return jsonify({
            "success": True,
            "desc": desc
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        })