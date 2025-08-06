from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

@app.route('/')
def home():
    return 'サーバ接続成功！'

# Render対応
if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)