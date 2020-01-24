import jwt
from .credentials import UserDetails
class Routes:
    def get_data(self):
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


    def post_data(self):
        user_details = UserDetails
        if self.path == '/register':
            user_details.for_registration(self)

        if self.path == '/login':
            user_details.for_login(self)

        if self.path == '/forgotpassword':
            user_details.forgot_password(self)

        elif 'new' in self.path:

            from urllib.parse import urlparse, parse_qs
            query_comp = parse_qs(urlparse(self.path).query)
            token = query_comp["new"][0]
            tokenn = jwt.decode(token, 'secret', algorithm='HS256')
            user_details.set_password(self, tokenn['email'])

        if self.path == '/note/api/createdata':
            user_details.create_data(self)

        if self.path == '/note/api/profilepicture':
            user_details.create_picture(self)

        if self.path == '/note/api/trash':
            user_details.is_trash(self)

        if self.path == '/note/api/pinned':
            user_details.is_pinned(self)

        if self.path == '/note/api/archive':
            user_details.is_archive(self)


    def put_data(self):
        if self.path == '/note/api/update':
            user_details = UserDetails
            user_details.update_data(self)


    def delete_data(self):
        user_details = UserDetails
        if self.path == '/note/api/delete':
            user_details.delete_data(self)

