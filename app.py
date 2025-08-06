from flask import Flask, request, jsonify, render_template
import json

app = Flask(__name__)

THRESHOLD_FILE = "threshold.json"

@app.route('/')
def index():
    return render_template('liff.html')

@app.route('/set_threshold', methods=['POST'])
def set_threshold():
    data = request.json
    with open(THRESHOLD_FILE, 'w') as f:
        json.dump(data, f)
    return jsonify({"status": "success"}), 200

@app.route('/get_threshold', methods=['GET'])
def get_threshold():
    try:
        with open(THRESHOLD_FILE, 'r') as f:
            data = json.load(f)
        return jsonify(data), 200
    except FileNotFoundError:
        return jsonify({"x_threshold": 0.5}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)