#!/usr/bin/env python3
"""
Example: Stateful chat with ai.sooners.us using gemma3:4b model.

Requires:
  pip install requests python-dotenv
"""

import os
import requests
from dotenv import load_dotenv

# Load API key and base URL from ~/.soonerai.env
load_dotenv(os.path.join(os.path.expanduser("~"), ".soonerai.env"))

API_KEY = os.getenv("SOONERAI_API_KEY")
BASE_URL = os.getenv("SOONERAI_BASE_URL", "https://ai.sooners.us").rstrip("/")
MODEL = os.getenv("SOONERAI_MODEL", "gemma3:4b")

if not API_KEY:
    raise RuntimeError("Missing SOONERAI_API_KEY in ~/.soonerai.env")

url = f"{BASE_URL}/api/chat/completions"

# Keep a conversation history
history = [
    {
        "role": "system",
        "content": "You are SpongeBob SquarePants. Speak cheerfully and use ocean humor.",
    }
]

MAX_TURNS = 5  # number of user+assistant pairs to retain

def chat(user_message: str):
    """Append user message, call API with full history, append assistant reply."""
    global history

    # Append user message
    history.append({"role": "user", "content": user_message})

    # Optionally trim old messages (keep system + last N pairs)
    if len(history) > 1 + MAX_TURNS * 2:
        history = [history[0]] + history[-MAX_TURNS * 2 :]

    payload = {
        "model": MODEL,
        "messages": history,
        "temperature": 0.6,
    }

    # Send POST request
    response = requests.post(
        url,
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
        },
        json=payload,
        timeout=60,
    )

    if response.status_code == 200:
        data = response.json()
        reply = data["choices"][0]["message"]["content"]
        print("SpongeBob:", reply)
        # Add assistant reply to history
        history.append({"role": "assistant", "content": reply})
    else:
        print(f"Error {response.status_code}: {response.text}")

# program loop
if __name__ == "__main__":
    print("Chat with SpongeBob! (type 'exit' to quit)\n")
    while True:
        user_msg = input("You: ").strip()
        if user_msg.lower() in {"exit", "quit"}:
            break
        chat(user_msg)
