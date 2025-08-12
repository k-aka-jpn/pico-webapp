from flask import Flask, request, jsonify, send_file
import json
import os

app = Flask(__name__)

THRESHOLD_FILE = "threshold.json"
DEFAULT_THRESHOLD = {"x_threshold": 0.5}

@app.route('/')
def index():
    # HTMLファイルが存在しない場合の安全対策
    if os.path.exists('liff.html'):
        return send_file('liff.html')
    else:
        return "<h1>LIFF HTML file not found</h1>", 404

@app.route('/set_threshold', methods=['POST'])
def set_threshold():
    try:
        data = request.json
        # JSON形式で保存
        with open(THRESHOLD_FILE, 'w') as f:
            json.dump(data, f)
        return jsonify({"status": "success"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/get_threshold', methods=['GET'])
def get_threshold():
    try:
        if not os.path.exists(THRESHOLD_FILE) or os.path.getsize(THRESHOLD_FILE) == 0:
            return jsonify(DEFAULT_THRESHOLD), 200

        with open(THRESHOLD_FILE, 'r') as f:
            data = json.load(f)
        return jsonify(data), 200
    except (FileNotFoundError, json.JSONDecodeError):
        return jsonify(DEFAULT_THRESHOLD), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    # Render では必ず 0.0.0.0 でポートを指定
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=False)