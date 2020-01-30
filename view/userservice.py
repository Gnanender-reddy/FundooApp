"""
@Author : P.Gnanender Reddy
@Since : Dec'2019
@:keyword:smtp,cgi(common graphical interface).
"""
import cgi
import jwt
from services.users import User

import cgitb;

cgitb.enable()
class UserDetails:



    def for_registration(self):
        form = cgi.FieldStorage(
        fp=self.rfile,
        headers=self.headers,
        environ={'REQUEST_METHOD':'POST','CONTENT_TYPE':self.headers['Content-Type'],}
        )

        data={'email':form['email'].value,'password':form['password'].value,'confirmpassword':form['confirmpassword'].value}
        user = User()
        response_data = user.register(data)
        return response_data

    def for_login(self):
        """
        This function is used for login process.
        """
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST',
                     'CONTENT_TYPE': self.headers['Content-Type'],
                     })
        data={'email':form['email'].value,'password':form['password'].value}
        user = User()
        response_data = user.login(data)
        return response_data

    def forgot_password(self, version):
        """
        This function is used for forgot password process.
        """
        form=cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD':'POST','CONTENT_TYPE':self.headers['Content-Type'],}
        )
        version=version.split('/')[0]
        host = self.headers['Host']

        data={'email':form['email'].value}
        response_data = self.user.forgot(data,host,version)
        return response_data




    def  set_password(self,email_id):

        print(self.headers)

        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST',
                     'CONTENT_TYPE': self.headers['Content-Type'],
                     })

        form_keys = list(form.keys())
        data = {'password': form['password'].value}
        user=User()

        response_data =user.resett(data,form_keys,email_id)
        return response_data



    def create_picture(self):
        ctype, pdict = cgi.parse_header(self.headers.get('content-type'))
        pdict['boundary'] = bytes(pdict['boundary'], "utf-8")
        if ctype == 'multipart/form-data':
            form = cgi.FieldStorage(fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST',
            'CONTENT_TYPE': self.headers['Content-Type'],
                    })
            filename = form['upfile'].filename
            data = form['upfile'].file.read()
            open("./media/%s" % filename, "wb").write(data)
            token = self.headers['token']
            payload = jwt.decode(token, "secret", algorithms='HS256')
            user_id = str(payload['id'])
            profile_data = {
                'profile_path': f'./media/{filename}',
                'user_id': user_id
                    }
            user=User()
            response_data = user.profile_picture(profile_data)
            return response_data







