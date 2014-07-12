#!/usr/bin/env python

import SimpleHTTPServer
import SocketServer

PORT = 8000

class MyHandler (SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET (s):
        print(dir(s))
        return SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(s)


httpd = SocketServer.TCPServer(("", PORT), MyHandler)

print "serving at port", PORT
httpd.serve_forever()
