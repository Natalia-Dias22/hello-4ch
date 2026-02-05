from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'OK'}), 200

# NOVO ENDPOINT! v2
@app.route('/version', methods=['GET'])
def version():
    return jsonify({
        'version': '2.0',
        'app': 'hello-4ch',
        'status': 'running'
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)