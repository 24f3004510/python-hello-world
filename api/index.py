from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
       # Parse the URL
        parsed_url = urlparse(self.path)

        # Extract query parameters
        query_params = parse_qs(parsed_url.query)

        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        response_body = "Request Parameters:\n"
        
        for key, value in query_params.items():
            response_body += f"{key}: {value}\n"
        self.wfile.write(response_body.encode('utf-8'))
        return
