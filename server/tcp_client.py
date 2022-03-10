import socket

class TcpClient:

    def __init__(self):
        # Note that the server may listen on a specific address or any address
        # (signified by the empty string), but the client must specify an address to
        # connect to. Here, we're connecting to the server on the same machine
        # (127.0.0.1 is the "loopback" address).
        self.SERVER_ADDRESS = '127.0.0.1'
        self.SERVER_PORT = 5080

        # Create the socket
        self._conn = socket.socket()

    def connect(self):
        # Connect to the server. A port for the client is automatically allocated
        # and bound by the operating system
        self._conn.connect((self.SERVER_ADDRESS, self.SERVER_PORT))

        print("Connected to " + str((self.SERVER_ADDRESS, self.SERVER_PORT)))

    def close(self):
        self._conn.close()

    def send_message(self, message):
        # Convert string to bytes. (No-op for python2)
        data = message.encode()

        # Send data to server
        self._conn.send(data)

        # Receive response from server
        data = self._conn.recv(2048)
        if not data:
            print("Server abended. Exiting")
            return

        # Convert back to string for python3
        data = data.decode()

        print("Got this string from server:")
        print(data + '\n')
