from http.server import BaseHTTPRequestHandler, HTTPServer
import os

class CORSRequestHandler(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_GET(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Content-Type", "text/html")
        self.end_headers()

        path = self.path[1:]  # remove leading slash
        if not path:
            path = "index.html"  # default to index.html if no path is specified

        if os.path.exists(path):
            with open(path, "rb") as f:
                self.wfile.write(f.read())
        else:
            self.wfile.write(b"File not found")

    def do_POST(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(b'{"message": "Sign up successful"}')

def run_server():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, CORSRequestHandler)
    print("Server running on port 8000...")
    httpd.serve_forever()

run_server()