from flask import Flask, request, jsonify
from flask_cors import CORS
import datetime

app = Flask(__name__)
CORS(app)  # Lets YƐƐ Talk call this server

# Baobab Knowledge Base
GHANA_REPLIES = {
    "hello": "Akwaba! YƐƐ AI here. How can Baobab Tech help you, Boss?",
    "how are you": "I dey fine. System 100%. Your YƐƐ Talk is live!",
    "time": f"Baobab time is {datetime.datetime.now().strftime('%H:%M')}. Accra never sleeps.",
    "what is yeetalk": "YƐƐ Talk = Ghana's first P2P video app. No data, no signup. Built by you.",
    "who built you": "CEO Kwame built me with Baobab Tech. I'm proud to serve Ghana.",
    "twi": "Mepa wo kyɛw, meka Twi kakra. YƐƐ Talk yɛ yɛn dea!",
}

@app.route('/ask', methods=['POST'])
def ask_ai():
    user_question = request.json.get('question', '').lower()
    
    # Check Baobab Knowledge first
    for key, reply in GHANA_REPLIES.items():
        if key in user_question:
            return jsonify({"answer": reply})
    
    # Default Baobab reply
    return jsonify({"answer": "YƐƐ AI is learning. But YƐƐ Talk Core is ready. Ask me about YƐƐ Talk, time, or say 'hello'."})

@app.route('/')
def home():
    return "YƐƐ AI Satellite Online. Baobab Tech reporting for duty."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)