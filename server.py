from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import html
from os import curdir, sep

last_one = ''

# HTTPRequestHandler class
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):
    
    # GET
    def do_GET(self):
        if not '.' in self.path.split('/')[-1] and self.path[-1] != '/':
            self.path+='/'
        if self.path.endswith('/'):
            self.path+="index.html"
        try:
            #Check the file extension required and
            #set the right mime type

            sendReply = True
            if self.path.endswith(".html"):
                mimetype='text/html'
            elif self.path.endswith(".jpg"):
                mimetype='image/jpg'
            elif self.path.endswith(".gif"):
                mimetype='image/gif'
            elif self.path.endswith(".js"):
                mimetype='application/javascript'
            elif self.path.endswith(".css"):
                mimetype='text/css'
            else:
                sendReply=False

            if sendReply == True:
                #Open the static file requested and send it
                f = open(curdir+sep+self.path,'rb') 
                self.send_response(200)
                self.send_header('Content-type',mimetype)
                self.end_headers()
                self.wfile.write(f.read())
                f.close()
            return

        except IOError:
            self.send_error(404,'File Not Found: {}'.format(self.path))
        return
        
    def do_POST(self):
        global last_one
        content_len=int(self.headers.get('content-length',0))
        post_body = self.rfile.read(content_len)
        post_body = post_body.decode()
        equal=(post_body==last_one)
        last_one=post_body
        print(post_body)
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.send_message(str(equal))
    
    def send_message(self,message):
        self.wfile.write(bytes(html.escape(message), "utf8"))
 
def run():
    print('starting server...')

    # Server settings
    # Choose port 8080, for port 80, which is normally used for a http server, you need root access
    server_address = ('127.0.0.1', 8080)
    httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
    print('running server...')
    httpd.serve_forever()

run()
