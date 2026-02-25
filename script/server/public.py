import http.server
import socketserver
import os

def sekai_server(OUT, port = 0):
    if port == 0:
        import random
        port = random.randint(9999, 65535)
    os.chdir(OUT)
    Handler = http.server.SimpleHTTPRequestHandler

    with socketserver.TCPServer(("", port), Handler) as httpd:
        print(f"Serving at: http://localhost:{port}")
        httpd.serve_forever()

