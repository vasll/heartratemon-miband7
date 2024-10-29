from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS on the app

heart_rate: str = 'N/A'

@app.route('/', methods=['POST'])
def update_heart_rate():
    global heart_rate
    data = request.form
    heart_rate = next(iter(data)).split(',')[1]
    print(f'heart_rate: {heart_rate}')
    return ('', 200)

@app.route('/', methods=['GET'])
def get_heart_rate():
    global heart_rate
    return jsonify({"heart_rate": heart_rate}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8081)
