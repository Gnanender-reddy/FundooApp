"""
@Author : P.Gnanender Reddy
@Since : Dec'2019
@Description:This response class is used for sending the response according to data.
"""
import json
class Response:

    def __init__(self, that):
        self.Response = that

    def jsonResponse(self, status, data):
        """
        This funciton is used for generating json response.
        """
        print(self.Response, '-------->')
        self.Response.send_response(status)
        self.Response.send_header('Content-type', 'text/json')
        self.Response.end_headers()
        self.Response.wfile.write(json.dumps(data).encode())

    def html_response(self, status, data):
        """
        This function is used sending HTMl response.
        """
        self.Response.send_response(status)
        self.Response.send_header('Content-type', 'text/html')
        self.Response.end_headers()
        self.Response.wfile.write(data.encode("utf8"))
