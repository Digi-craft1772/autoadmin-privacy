from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/privacy-policy', methods=['GET'])
def privacy_policy():
    return jsonify({
        'privacy_policy': 'This is where the privacy policy text will go.'
    })

@app.route('/terms-of-service', methods=['GET'])
def terms_of_service():
    return jsonify({
        'terms_of_service': 'This is where the terms of service text will go.'
    })

if __name__ == '__main__':
    app.run(debug=True)