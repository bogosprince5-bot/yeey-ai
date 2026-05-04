from flask import Flask, request, jsonify, render_template_string
from flask_cors import CORS
import datetime
import os
import logging

app = Flask(__name__)
CORS(app)
logging.basicConfig(level=logging.INFO)

HTML = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>YƐƐ AI - Baobab Tech</title>
    <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>🌳</text></svg>">
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
            <span class="badge">v1.3 Live</span>
            <span class="badge">Frankfurt</span>
            <span class="badge">Ghana AI</span>
        </div>
        <div class="stats">
            <p><strong>Deployed:</strong> May 4, 2026</p>
            <p><strong>Origin:</strong> Accra, Ghana</p>
            <p><strong>Stack:</strong> Python + Flask + Render</p>
            <p><strong>API:</strong> /ask endpoint active</p>
