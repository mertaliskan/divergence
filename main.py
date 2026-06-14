import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
SECRET = os.getenv("WEBHOOK_SECRET")

@app.route("/")
def home():
    return "Bot çalışıyor"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json

    if data.get("secret") != SECRET:
        return jsonify({"error": "wrong secret"}), 401

    msg = f"""
🚨 Positive Regular Divergence

Hisse: {data.get("symbol")}
Fiyat: {data.get("price")}
Zaman: {data.get("time")}
Periyot: {data.get("interval")}
"""

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    requests.post(url, json={
        "chat_id": CHAT_ID,
        "text": msg
    })

    return jsonify({"ok": True})
