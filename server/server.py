"""
@Author : P.Gnanender Reddy
@Since : Dec'2019
@Description: This code is for creating HTTP server This class is used to handle the HTTP requests that arrive at the ser
ver. By itself, it cannot respond to any actual HTTP requests; it must be subclassed to handle each request method
(e.g. GET or POST). BaseHTTPRequestHandler provides a number of class and instance variables, and methods for use by sub-
-classes.
"""
import sys
from http.server import HTTPServer, SimpleHTTPRequestHandler
import jwt

sys.path.insert(0,'/home/admin1/PycharmProjects/FundooApp/')

from view.credentials import UserDetails


# Defining a HTTP request Handler class
class Server(SimpleHTTPRequestHandler):
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
        return content.encode("utf8")  # NOTE: must return a bytes object!


    def do_GET(self):
        """
        This do_get method is used to request data from server.

        """
        self._set_headers()

        if self.path =='/register':
            print("inside get method")
            with open("templates/registration.html") as file:
             html_string_register = file.read()
             self.wfile.write(self._html(html_string_register))

        if self.path=='/login':
            with open("templates/login.html") as file:
                html_string_login=file.read()
            self.wfile.write(self._html(html_string_login))

        if self.path=='/forgotpassword':
            with open("templates/forgotpassword.html") as file:
                html_string_fp=file.read()
                self.wfile.write(self._html(html_string_fp))

        elif 'new' in self.path:
            from urllib.parse import urlparse, parse_qs
            query_comp = parse_qs(urlparse(self.path).query)
            token = query_comp["new"][0]
            with open('templates/resetpassword.html') as f:
                html_string_register = f.read()
                output = html_string_register.format(result=token)
                self.wfile.write(self._html(output))

        if self.path == '/read':
            user_details=UserDetails
            user_details.read(self)





    def do_PUT(self):
        """
        This function do all crud(create, read, update, delete) operations  here.

        """
        if self.path == '/update':
            user_details= UserDetails
            user_details.update(self)




    def do_DELETE(self):
        user_details= UserDetails
        if self.path == "/delete":
            user_details.delete(self)


    def do_POST(self):
        """

        This do_post method is used for submitting the data to be processed to server.
        """
        user_details = UserDetails
        if self.path == '/register':
            user_details.register(self)

        if self.path=='/login':
            user_details.login(self)

        if self.path=='/forgotpassword':
            user_details.forget(self)

        elif 'new' in self.path:

            from urllib.parse import urlparse, parse_qs
            query_comp = parse_qs(urlparse(self.path).query)
            token = query_comp["new"][0]
            tokenn = jwt.decode(token, 'secret', algorithm='HS256')
            user_details.set_password(self, tokenn['email'])

        if self.path=='/create':
            user_details.create(self)

        if self.path=='/pro':
            user_details.create_pic(self)

        if self.path=='/trash':
            user_details.isTrash(self)

        if self.path == '/pinned':
            user_details.isPinned(self)

        if self.path == '/archive':
            user_details.isArchive(self)

def run(server_class=HTTPServer, handler_class=Server, addr="localhost", port=8080):
    """
    This function is used for running the server class.
    """
    server_address = (addr, port)
    httpd = server_class(server_address, handler_class)

    print(f"httpd server on {addr}:{port}")
    httpd.serve_forever()

if __name__ == '__main__':
    run(HTTPServer, Server, "localhost", 8080)






