import http.server
import socketserver
import platform
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

def try_kill_port(port):
    system = platform.system()
    
    if system == "Windows":
        result = os.popen(f'netstat -ano | findstr :{port}').read()
        for line in result.split('\n'):
            if 'LISTENING' in line:
                pid = line.strip().split()[-1]
                os.system(f'taskkill /F /PID {pid} >nul 2>&1')
    else:
        pids = os.popen(f'ss -lptn sport = :{port} 2>/dev/null | grep -o "pid=\\S*" | cut -d= -f2').read().strip()
        if not pids:
            pids = os.popen(f'netstat -tlnp 2>/dev/null | grep :{port} | awk \'{{print $7}}\' | cut -d/ -f1').read().strip()
        if not pids:
            pids = os.popen(f'lsof -ti:{port} 2>/dev/null').read().strip()
        if pids:
            for pid in pids.split('\n'):
                os.system(f'kill -9 {pid} 2>/dev/null')

