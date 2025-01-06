from flask import Flask, jsonify
from dendrite_sdk import AsyncDendrite
from dendrite_sdk.remote import BrowserbaseConfig
import subprocess

app = Flask(__name__)

@app.route('/')
async def run_dendrite_auth():
    try:
        browser = AsyncDendrite(auth=["youtube.com"], dendrite_api_key="sk_d6aacf77ee8acba13ce14c8da02e1c7f22e7c9b83451ffb80ed7b2a9b5f97028", playwright_options={ "headless": True})

        await browser.goto(
            "https://youtube.com",
            expected_page="You should be logged in with the youtube feed visible",
        )
        desc = await browser.ask("List the recommended video topics")
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