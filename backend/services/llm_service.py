import os
import requests
from dotenv import load_dotenv
import json
import re

load_dotenv()

API_KEY = os.getenv("CEREBRAS_API_KEY")

def clean_llm_output(text: str):
    # Remove markdown code block formatting
    text = re.sub(r"```json", "", text)
    text = re.sub(r"```", "", text)
    return text.strip()

def call_llm(prompt: str):

    url = "https://api.cerebras.ai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama3.1-8b",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.4
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code != 200:
        return ""

    content = response.json()["choices"][0]["message"]["content"]
    cleaned = clean_llm_output(content)

    return cleaned