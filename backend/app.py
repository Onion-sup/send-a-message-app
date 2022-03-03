from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_socketio import SocketIO

# instantiate the app
app = Flask(__name__, static_folder='../frontend/build/', static_url_path='/')
app.config.from_object(__name__)

socketio = SocketIO(app)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/api/send-message', methods=['POST'])
def post_message():
    response_object = {'status': 'success'}
    post_data = request.get_json()
    print(post_data)
    socketio.emit("message", post_data)
    response_object['message'] = 'Message sent'
    return jsonify(response_object)

if __name__ == '__main__':
    socketio.run(app)
