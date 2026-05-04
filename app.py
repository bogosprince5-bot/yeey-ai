from flask import Flask, request, jsonify, render_template_string
from flask_cors import CORS
import datetime
import os

app = Flask(__name__)
CORS(app)  # Lets Yɛɛ Talk call this API

HTML = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>YƐƐ AI - Baobab Tech</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            background: linear-gradient(135deg, #0d1117 0%, #161b22 100%);
            color: #c9d1d9;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif;
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            padding: 20px;
        }
        .container { max-width: 600px; animation: fadeIn 1s ease-in; }
        .logo { font-size: 4rem; margin-bottom: 20px; animation: pulse 2s infinite; }
        h1 { font-size: 3rem; color: #58a6ff; margin-bottom: 10px; letter-spacing: 2px; }
        h2 { font-size: 1.5rem; color: #7ee787; margin-bottom: 30px; font-weight: 300; }
        .badge { display: inline-block; background: #238636; color: white; padding: 8px 16px; border-radius: 20px; font-size: 0.9rem; margin: 10px 5px; }
        .stats { margin-top: 40px; padding-top: 30px; border-top: 1px solid #30363d; font-size: 0.9rem; color: #8b949e; }
        .footer { margin-top: 30px; font-size: 0.8rem; color: #484f58; }
        @keyframes fadeIn { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }
        @keyframes pulse { 0%, 100% { transform: scale(1); } 50% { transform: scale(1.1); } }
    </style>
</head>
<body>
    <div class="container">
        <div class="logo">🌳</div>
        <h1>YƐƐ AI</h1>
        <h2>Satellite Online. Baobab Tech reporting for duty.</h2>
        <div>
            <span class="badge">v1.2 Live</span>
            <span class="badge">Frankfurt</span>
            <span class="badge">Ghana AI</span>
        </div>
        <div class="stats">
            <p><strong>Deployed:</strong> May 3, 2026</p>
            <p><strong>Origin:</strong> Accra, Ghana</p>
            <p><strong>Stack:</strong> Python + Flask + Render</p>
            <p><strong>API:</strong> /ask endpoint active</p>
        </div>
        <div class="footer">
            <p>Founded by CEO Kwame. Powered by the Ɛ.</p>
            <p>https://yee-ai.onrender.com</p>
        </div>
    </div>
</body>
</html>
'''

# Baobab Knowledge Base
GHANA_REPLIES = {
    "hello": "Akwaba! YƐƐ AI here. How can Baobab Tech help?",
    "how are you": "I dey fine. System green. YƐƐ AI operational.",
    "time": f"Baobab time is {datetime.datetime.now().strftime('%H:%M:%S')}",
    "what is yeetalk": "YƐƐ Talk = Ghana's AI chat. Built by CEO Kwame.",
    "who built you": "CEO Kwame built me for Baobab Tech. From Accra to the world.",
    "twi": "Mepa wo kyɛw, meka Twi kakra. YƐƐ AI learns fast."
}

@app.route('/')
def home():
    return render_template_string(HTML)

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
