# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)

OPENAI_API_KEY = 
headers = {
    "Authorization": f"Bearer {OPENAI_API_KEY}"
}

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    print(data)
    prompt = data.get("prompt")
    try:
        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers=headers,
            json={
                "model": "ft:gpt-3.5-turbo-0125:personal:dukeeces:96D8orkb",
                "messages": [{"role": "user", "content": prompt}]
            }
        )
        response.raise_for_status()  # This will raise an exception for HTTP error codes
        chat_response = response.json()
        return jsonify(chat_response)
    except requests.RequestException as e:
        print(e)
        return jsonify({"error": "Failed to communicate with OpenAI API"}), 500

if __name__ == '__main__':
    app.run(debug=True)
