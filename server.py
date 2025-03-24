from flask import Flask, jsonify
from flask_cors import CORS  
import subprocess
import os

app = Flask(__name__)
CORS(app)  # ✅ Allow cross-origin requests

@app.route('/update', methods=['POST'])
def update_github():
    try:
        # Run your script to fetch and push updates
        main_script_path = os.path.join(os.path.dirname(__file__), "main.py")
        result = subprocess.run(["/opt/homebrew/bin/python3.10", main_script_path], capture_output=True, text=True)

        print(result.stderr)  # Add this for debugging

        if result.returncode == 0:
            return jsonify({"message": "GitHub updated successfully!"}), 200
        else:
            return jsonify({"error": "Script failed", "details": result.stderr}), 500
    
    except Exception as e:
        return jsonify({"error": "Server error", "details": str(e)}), 500
    
@app.route('/update', methods=['GET'])
def update_info():
    return "This API only accepts POST requests. Use curl or Postman to send a POST request.", 405

    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)


