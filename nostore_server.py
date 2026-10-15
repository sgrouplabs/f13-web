from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

os.chdir("public")

class H(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

HTTPServer(("", 5200), H).serve_forever()
