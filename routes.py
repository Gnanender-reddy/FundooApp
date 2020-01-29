from http.server import SimpleHTTPRequestHandler

import jwt

from auth.login_authentication import is_authenticated
from view.noteservices import NoteDetails
from view.response import Response
from view.userservice import UserDetails


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
        if self.path == '/register':
            with open("templates/registration.html") as file:
                html_string_register = file.read()
                self.wfile.write(self._html(html_string_register))

        if self.path == '/login':
            with open("templates/login.html") as file:
                html_string_login = file.read()
            self.wfile.write(self._html(html_string_login))

        if self.path == '/forgotpassword':
            with open("templates/forgotpassword.html") as file:
                html_string_fp = file.read()
                self.wfile.write(self._html(html_string_fp))

        elif 'new' in self.path:
            from urllib.parse import urlparse, parse_qs
            query_comp = parse_qs(urlparse(self.path).query)
            token = query_comp["new"][0]
            with open('templates/resetpassword.html') as f:
                html_string_register = f.read()
                output = html_string_register.format(result=token)
                self.wfile.write(self._html(output))
        elif self.path == '/note/api/read':
            user_details = UserDetails
            user_details.read_data(self)

    @is_authenticated
    def do_PUT(self):
        """
        This function is used for updating data in the database.
        """
        note_details = NoteDetails
        if self.path == '/note/api/update':
            response_data=note_details.update_data(self)
            Response(self).jsonResponse(status=200, data=response_data)

    @is_authenticated
    def do_DELETE(self):
        """
        This function is used for deleting the data from the database.
        """
        note_details = NoteDetails
        if self.path == '/note/api/delete':
            response_data=note_details.delete_data(self)
            Response(self).jsonResponse(status=200, data=response_data)


    @is_authenticated
    def do_POST(self):
        """
        This do_post method is used for submitting the data to be processed to server.
        """
        version = self.protocol_version
        user_details = UserDetails
        note_details=NoteDetails

        if self.path == '/register':
            response_data = user_details.for_registration(self)
            Response(self).jsonResponse(status=200, data=response_data)

        if self.path == '/login':
            response_data=user_details.for_login(self)
            Response(self).jsonResponse(status=200, data=response_data)


        if self.path == '/forgotpassword':
            user_details.forgot_password(self, version)

        elif 'new' in self.path:

            from urllib.parse import urlparse, parse_qs
            query_comp = parse_qs(urlparse(self.path).query)
            token = query_comp["new"][0]
            tokenn = jwt.decode(token, 'secret', algorithm='HS256')
            user_details.set_password(self, tokenn['email'])

        if self.path == '/note/api/createdata':
            responsee=note_details.create_data(self)
            Response(self).jsonResponse(status=200, data=responsee)


        if self.path == '/note/api/profilepicture':
            user_details.create_picture(self)

        if self.path == '/note/api/trash':
            user_details.is_trash(self)

        if self.path == '/note/api/pinned':
            user_details.is_pinned(self)

        if self.path == '/note/api/archive':
            user_details.is_archive(self)



