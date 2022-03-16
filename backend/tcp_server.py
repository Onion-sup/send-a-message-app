#!/usr/bin/env python
"""
An annotated simple socket server example in python.

WARNING: This example doesn't show a very important aspect of
TCP - TCP doesn't preserve message boundaries. Please refer
to http://blog.stephencleary.com/2009/04/message-framing.html
before adapting this code to your application.

Runs in both python2 and python3.
"""

import socket
import json
from datetime import datetime
import time, sys, threading

class TcpServer:
    def __init__(self, port):
        self.sock = socket.socket()

        # Optional: this allows the program to be immediately restarted after exit.
        # Otherwise, you may need to wait 2-4 minutes (depending on OS) to bind to the
        # listening port again.
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind(('', port))

        # How many "pending connections" may be queued. Exact interpretation of this
        # value is complicated and operating system dependent. This value is usually
        # fine for an experimental server.
        self.sock.listen(5)
        self.conn = None
        self.server_thread = None
        self.stop_event = threading.Event()

    def run(self):
        self.stop_event.clear()
        while not self.stop_event.is_set():
            self.conn, addr = self.sock.accept()
            print("\nConnection received from %s" % str(addr))
            while not self.stop_event.is_set():
                data = self.conn.recv(2048)
                if not data:
                    print("End of file from client. Resetting")
                    break
            self.conn.close()

    def start(self):
        self.server_thread = threading.Thread(target=self.run)
        self.server_thread.start()

    def stop(self):
        if self.server_thread:
            self.stop_event.set()
            self.server_thread.join()

    def send_data(self, data_dict):
        if self.conn:
            print('[TcpServer][send_data] {}'.format(data_dict))
            data_str = json.dumps(data_dict)
            self.conn.send(data_str.encode())
    