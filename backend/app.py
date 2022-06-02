import threading
from flask import Flask, jsonify, request
from flask_cors import CORS

# instantiate the app
app = Flask(__name__, static_folder='../frontend/dist/', static_url_path='/')
app.config.from_object(__name__)

# enable COR
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/')
def index():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run()

    