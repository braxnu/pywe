#!/usr/bin/env python

import SimpleHTTPServer
import SocketServer

PORT = 8000

class MyHandler (SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET (s):
        for key in dir(s):
            if hasattr(s, key):
                print(key + ': ' + str(getattr(s, key))[:80])

        return SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(s)


httpd = SocketServer.TCPServer(("", PORT), MyHandler)

print "serving at port", PORT
httpd.serve_forever()
