# -*- coding: utf-8 -*-
'''
    :file: server.py
    :author: -Farmer
    :url: https://blog.farmer233.top
    :date: 2022/04/03 10:55:28
'''
import socket

class HTTPServer():

    def __init__(self, server_address:str="127.0.0.1:5000") -> None:
        self.addr = server_address
        self.request_queue_size = 5
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            self._bind()
            self._activate()
        except:
            self._close()
            raise

    def _bind(self):
        # self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind(self.addr)
    
    def _activate(self):
        self.socket.listen(self.request_queue_size)
    
    def _close(self):
        self.socket.close()
    
    def server_forever(self, poll_interval=0.5):
        while True:
            request_client, sock_addr = self.socket.accept()
            # 处理请求
    
    def _process_request(self, request, client_address):
        pass
            
class HTTPRequestHandler():
    def __init__(self, request:socket.socket, client_address, server) -> None:
        self.request = request
        self.rfile = self.request.makefile('rb', -1)
        self.wfile = self.request.makefile('wb', 0)
        pass
    
    def handle(self):
        self.raw_requestline_bytes = self.rfile.readline(65537)
        requestline = self.raw_requestline_bytes.decode('utf-8')
        requestline = requestline.strip('\r\n')
        self.method, self.path, self.request_version = requestline.split()
        self.headers = self.parse_headers()
    
    def parse_headers(self) -> dict:
        headers = {}
        while True:
            line = self.rfile.readline()
            if line in (b'\r\n', b'\n', b''):
                break
            line_str = line.decode('utf-8')
            k, v = line_str.split(': ')
            headers[k] == v
        return headers


        pass

    def finish(self):
        self.wfile.flush()
        self.wfile.close()

class RequestHandler():
    pass
