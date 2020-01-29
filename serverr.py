"""
@Author : P.Gnanender Reddy
@Since : Dec'2019
@Description: This code is for creating HTTP server, this class is used to handle the HTTP requests that arrive at the
server. By itself, it cannot respond to any actual HTTP requests, it must be subclassed to handle each request method
(e.g. GET or POST). SimpleHTTPRequestHandler provides a number of class and instance variables, and methods for use by
sub-classes.
"""
import os
from http.server import HTTPServer
from routes import ServiceHandler

if __name__ == '__main__':
    server =HTTPServer((os.getenv("SERVER_HOST_IP_ADDRESS"),int(os.getenv("SERVER_HOST_PORT"))),ServiceHandler)
    print(f"httpd server start on {os.getenv('SERVER_HOST_IP_ADDRESS')}:{int(os.getenv('SERVER_HOST_PORT'))}")
    server.serve_forever()




