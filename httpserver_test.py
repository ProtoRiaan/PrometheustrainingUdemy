import http.server
from prometheus_client import start_http_server, Counter

REQUESTS = Counter('test_request_total', 'This is a counter test metric for Total Get requests')

class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        REQUESTS.inc()
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"test")

if __name__ == "__main__":
    start_http_server(5001)
    server =http.server.HTTPServer(('192.168.222.14', 5000), MyHandler)
    server.serve_forever()


