from flask import Flask, request, jsonify, render_template
import json
import os

app = Flask(__name__)

# ファイル保存パス（サーバー起動ディレクトリ基準）
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
THRESHOLD_FILE = os.path.join(BASE_DIR, "threshold.json")

@app.route('/')
def index():
    # liff.html を templates フォルダから読み込む
    return render_template('liff.html')

@app.route('/set_threshold', methods=['POST'])
def set_threshold():
    try:
        data = request.json
        if not isinstance(data, dict):
            return jsonify({"status": "error", "message": "Invalid data format"}), 400
        with open(THRESHOLD_FILE, 'w') as f:
            json.dump(data, f)
        return jsonify({"status": "success"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/get_threshold', methods=['GET'])
def get_threshold():
    try:
        if not os.path.exists(THRESHOLD_FILE):
            # デフォルト値を返す
            return jsonify({"x_threshold": 0.5}), 200
        with open(THRESHOLD_FILE, 'r') as f:
            data = json.load(f)
        return jsonify(data), 200
    except json.JSONDecodeError:
        # JSON壊れ時はデフォルト値
        return jsonify({"x_threshold": 0.5}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    # 開発時のみデバッグON
    app.run(host='0.0.0.0', port=5000, debug=True)