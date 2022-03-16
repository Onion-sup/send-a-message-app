import threading
from flask import Flask, jsonify, request
from flask_cors import CORS
from tcp_server import TcpServer
tcp_server = TcpServer(5001)
tcp_server.start()
# instantiate the app
app = Flask(__name__, static_folder='../frontend/dist/', static_url_path='/')
app.config.from_object(__name__)

# enable COR
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/api/send-message', methods=['POST'])
def post_message():
    response_object = {'status': 'success'}
    post_data = request.get_json()
    print(post_data)
    tcp_server.send_data({'msg': 'hello'}) 
    response_object['message'] = 'Message sent'
    return jsonify(response_object)

if __name__ == '__main__':
    app.run()

    