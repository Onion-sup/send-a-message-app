import socketio

sio = socketio.Client()

@sio.event
def message(data):
    print('I received a message! {}'.format(data))

@sio.event
def connect():
    print("I'm connected!")

@sio.event
def connect_error(data):
    print("The connection failed!")

@sio.event
def disconnect():
    print("I'm disconnected!")

if __name__ == '__main__':
    sio.connect('http://localhost:5000', wait_timeout = 10)
