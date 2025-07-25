from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/generate', methods=['GET'])
def generate_otp():
    result = subprocess.run(['otp_handler.exe', 'generate'], capture_output=True, text=True)
    return jsonify({'message': result.stdout.strip()})

@app.route('/verify', methods=['POST'])
def verify_otp():
    otp = request.json.get('otp')
    result = subprocess.run(['otp_handler.exe', 'verify', otp], capture_output=True, text=True)
    return jsonify({'message': result.stdout.strip()})

if __name__ == '__main__':
    app.run(debug=True)
