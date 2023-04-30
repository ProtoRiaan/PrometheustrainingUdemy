import http.server
from prometheus_client import start_http_server

class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"test")

if __name__ == "__main__":
    start_http_server(5001)
    server =http.server.HTTPServer(('192.168.222.14', 5000), MyHandler)
    server.serve_forever()
