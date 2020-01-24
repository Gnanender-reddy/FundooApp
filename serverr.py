"""
@Author : P.Gnanender Reddy
@Since : Dec'2019
@Description: This code is for creating HTTP server, this class is used to handle the HTTP requests that arrive at the
server. By itself, it cannot respond to any actual HTTP requests, it must be subclassed to handle each request method
(e.g. GET or POST). SimpleHTTPRequestHandler provides a number of class and instance variables, and methods for use by
sub-classes.
"""
import os
from http.server import HTTPServer,SimpleHTTPRequestHandler
from view.routes import Routes
class ServiceHandler(SimpleHTTPRequestHandler):
    """
    This class is used to perform operations related to http request
    """
    def _set_headers(self):

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def _html(self, message):
        """
        This  function is used to generate an HTML document that includes `message`s
        in the body.
        """
        content = f"<html><body><h1>{message}</h1></body></html>"
        return content.encode("utf8")


    def do_GET(self):
        """
        This do_get method is used to request data from server.
        """
        self._set_headers()
        routes=Routes
        routes.get_data(self)

    def do_PUT(self):
        """
        This function is used for updating data in the database.
        """
        routes=Routes
        routes.put_data(self)

    def do_DELETE(self):
        """
        This function is used for deleting the data from the database.
        """
        routes=Routes
        routes.delete_data(self)

    def do_POST(self):
        """
        This do_post method is used for submitting the data to be processed to server.
        """
        routes=Routes
        routes.post_data(self)

server =HTTPServer((os.getenv("SERVER_HOST_IP_ADDRESS"),int(os.getenv("SERVER_HOST_PORT"))),ServiceHandler)
server.serve_forever()




