#!/usr/bin/env python3
from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        path = self.path.split('?')[0].split('#')[0]
        # If no extension and not a directory, try adding .html
        if '.' not in os.path.basename(path):
            candidate = path.rstrip('/') + '.html'
            if os.path.exists('.' + candidate):
                self.path = candidate
        super().do_GET()

    def end_headers(self):
        # Never cache HTML, CSS or JS so changes are always picked up immediately
        ext = os.path.splitext(self.path.split('?')[0])[1].lower()
        if ext in ('', '.html', '.css', '.js'):
            self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
            self.send_header('Pragma', 'no-cache')
            self.send_header('Expires', '0')
        super().end_headers()

HTTPServer(('', 3000), Handler).serve_forever()
