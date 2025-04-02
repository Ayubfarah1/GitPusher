from flask import Flask, jsonify
from flask_cors import CORS
import subprocess
import os

app = Flask(__name__)
CORS(app)

@app.route('/update', methods=['POST'])
def update_github():
    try:
        main_script = os.path.join(os.path.dirname(__file__), "main.py")
        result = subprocess.run(["python", main_script], capture_output=True, text=True)
        if result.returncode == 0:
            return jsonify({"message": "GitHub updated successfully!"}), 200
        else:
            return jsonify({"error": "Script failed", "details": result.stderr}), 500
    except Exception as e:
        return jsonify({"error": "Server error", "details": str(e)}), 500
@app.route('/update', methods=['GET'])
def info():
    return jsonify({"message": "Use POST to update"}), 405




if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
