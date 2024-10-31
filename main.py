from flask import Flask, request, jsonify
from flask_cors import CORS

ADDRESS = '0.0.0.0'
PORT = 8081
heart_rate: str = 'N/A'

app = Flask(__name__)
CORS(app)

""" Endpoint to update local heart_rate coming from phone """
@app.route('/', methods=['POST'])
def update_heart_rate():
    global heart_rate
    data = request.form # Contains `%antexts()` Tasker variable
    heart_rate = next(iter(data)).split(',')[1] # Extract only heart rate from notification
    print(f'RECEIVED heart_rate FROM TASKER: {heart_rate}')
    return ('', 200)

""" Endpoint to fetch the current heart rate, to be then displayed in the webapp """
@app.route('/', methods=['GET'])
def get_heart_rate():
    global heart_rate
    return jsonify({"heart_rate": heart_rate}), 200

if __name__ == "__main__":
    app.run(host=ADDRESS, port=PORT)
