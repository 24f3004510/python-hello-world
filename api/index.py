from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import json
class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        # read the data file
        file = open('q-vercel-python.json', 'r')
        data = file.read()
        data = json.loads(data)
        file.close()



       # Parse the URL
        parsed_url = urlparse(self.path)

        # Extract query parameters
        query_params = parse_qs(parsed_url.query)

        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        response_body = ""
        request_array = []
        marks_dict = {"marks" : []}

        for key, value in query_params.items():
            #response_body += f"{key}: {value}\n"
            if key == 'name':
                request_array = value

        for req in request_array:
            for dict in data:
                #print(type(dict))
                if dict["name"] == req:
                    marks_dict["marks"].append(dict["marks"])
                    break

        response_body += f"{str(marks_dict)}"
        self.wfile.write(response_body.encode('utf-8'))
        return
