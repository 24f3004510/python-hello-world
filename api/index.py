from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        # get the names request parameters
        # print(self.path)
        # print(self.headers)
        # print(self.requestline)
        # print(self.client_address)

        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        output = 'Hello, world!!!' + self.path + '\n' + str(self.headers) + '\n' + str(self.requestline) + '\n' + str(self.client_address) + '\n'
        self.wfile.write(output.encode('utf-8'))
        return
