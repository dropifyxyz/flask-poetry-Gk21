from flask import Flask, jsonify
from dendrite_sdk import Dendrite
import subprocess

app = Flask(__name__)

@app.route('/')
def run_dendrite_auth():
    try:
        # This will open the local browser
        process = subprocess.Popen(
            ["dendrite", "auth", "--url", "linkedin.com"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        stdout, stderr = process.communicate()

        browser = Dendrite(auth=["facebook.com", "instagram.com", "tiktok.com", "youtube.com", "linkedin.com"], dendrite_api_key="sk_d6aacf77ee8acba13ce14c8da02e1c7f22e7c9b83451ffb80ed7b2a9b5f97028", playwright_options={ "headless": True})

        browser.goto(
            "https://linkedin.com",
            expected_page="You should be logged in with the linkedin feed visible",
        )
        desc = browser.ask("Who was ")
        print("First post description: ", desc)

        
        return jsonify({
            "success": True,
            "desc": desc
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        })
