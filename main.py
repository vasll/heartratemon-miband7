from flask import Flask, request, jsonify
from flask_cors import CORS

ADDRESS = '0.0.0.0'
PORT = 8081
heart_rate: str = 'N/A'

app = Flask(__name__)
CORS(app)

""" Endpoint to update heart rate coming from phone (or any data source)"""
@app.route('/', methods=['POST'])
def update_heart_rate():
    global heart_rate
    data = request.form
    heart_rate = next(iter(data)).split(',')[1]
    print(f'heart_rate: {heart_rate}')
    return ('', 200)

"""Endpoint to fetch the current heart rate, to be then displayed in the webapp"""
@app.route('/', methods=['GET'])
def get_heart_rate():
    global heart_rate
    return jsonify({"heart_rate": heart_rate}), 200

if __name__ == "__main__":
    app.run(host=ADDRESS, port=PORT)
