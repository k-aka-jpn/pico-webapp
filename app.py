from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)
config_file = 'config.json'

@app.route('/set_config', methods=['POST'])
def set_config():
    data = request.json
    with open(config_file, 'w') as f:
        json.dump(data, f)
    return jsonify({"status": "ok", "received": data})

@app.route('/get_config', methods=['GET'])
def get_config():
    try:
        with open(config_file, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}
    return jsonify(data)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)