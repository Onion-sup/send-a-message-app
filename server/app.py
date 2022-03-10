import threading
from flask import Flask, jsonify, request
from flask_cors import CORS
import socket
from tcp_client import TcpClient 

# instantiate the app
app = Flask(__name__, static_folder='../client/frontend/dist/', static_url_path='/')
app.config.from_object(__name__)

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
    tcp_client.send_message("hello")
    response_object['message'] = 'Message sent'
    return jsonify(response_object)

if __name__ == '__main__':
    tcp_client = TcpClient()
    tcp_client.connect()
    app.run()
    tcp_client.close()
    