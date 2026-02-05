from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)


origins = [
    "https://hello-4ch-frontend-952043957190.us-east1.run.app",  
    "http://localhost:8081",
]

CORS(app, origins=origins)  

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'OK'}), 200

@app.route('/version', methods=['GET'])
def version():
    return jsonify({
        'version': '2.0',
        'app': 'hello-4ch',
        'status': 'running'
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)