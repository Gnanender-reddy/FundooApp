"""
@Author : P.Gnanender Reddy
@Since : Dec'2019
@:keyword:smtp,cgi(common graphical interface).
"""
import cgi
import jwt
from config.redis_connection import RedisService
from services.users import user
from vendor.smtp import smtp
from models.datamanagement import DataBaseMangament
from view.response import Response
import cgitb;
#from datetime import datetime, timedelta
from auth.login_authentication import response
# JWT_SECRET = 'secret'
# JWT_ALGORITHM = 'HS256'
# JWT_EXP_DELTA_SECONDS = 100000000
cgitb.enable()
class UserDetails:
    def for_registration(self):
        form = cgi.FieldStorage(
        fp=self.rfile,
        headers=self.headers,
        environ={'REQUEST_METHOD':'POST','CONTENT_TYPE':self.headers['Content-Type'],}
        )

        data={'email':form['email'].value,'password':form['password'].value,'confirmpassword':form['confirmpassword'].value}
        u=user()
        response_data = u.register(data)
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
        u = user()
        response_data = u.login(data)
        return response_data





        #         email = data['email']
        #         id, email = data_base_object.read_email(email=email)
        #         if id:
        #             payload = {'id': id,'exp': datetime.utcnow() + timedelta(seconds=JWT_EXP_DELTA_SECONDS)}
        #             encoded_token = jwt.encode(payload, 'secret', 'HS256').decode('utf-8')
        #             print(id, encoded_token)
        #             redis_obj = RedisService()
        #             redis_obj.set(id, encoded_token)
        #             print(redis_obj.get(id),'------------->r.get')
        #             res = response(success=True, message="Login Successfully", data=[{"token": encoded_token}])
        #             Response(self).jsonResponse(status=200, data=res)
        # else:
        #     Response(self).jsonResponse(status=400, data=response(message="credentials are missing"))

    def forgot_password(self, version):
        """
        This function is used for forgot password process.
        """
        form=cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD':'POST','CONTENT_TYPE':self.headers['Content-Type'],}
        )
        host = self.headers['Host']
        data_base_object=DataBaseMangament()
        data={'email':form['email'].value}
        respon={'success':None,'data':[],'message':""}
        if data_base_object.checkinguser(data['email']):
            email=data['email']
            s = smtp()
            encoded_jwt = jwt.encode({'email': email}, 'secret', algorithm='HS256').decode("UTF-8")
            data = f"{version}://{host}/reset/?new={encoded_jwt}"

            s.send_mail(email,data)

            respon.update({'success': True, 'data': [], 'message': "Message sent Successfully"})
            Response(self).jsonResponse(status=200, data=respon)
        else:

            respon.update({'success': False, 'data': [], 'message': "unsuccessfull"})
            Response(self).jsonResponse(status=404, data=respon)


    def  set_password(self,email_id):
        """
        processing user input submitted in Front end(HTML)
        """
        print(self.headers)

        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST',
                     'CONTENT_TYPE': self.headers['Content-Type'],
                     })
        responce_data = {'success': None, 'data': [], 'message': ""}
        form_keys = list(form.keys())
        data = {'password': form['password'].value,'confirmpassword':form['confirmpassword'].value}
        data_base_object=DataBaseMangament()
        if len(form_keys) < 2:
            responce_data.update({'success': False, 'data': [], 'message': "some values are missing"})
            Response(self).jsonResponse(status=404, data=responce_data)
        else:
            data_base_object.update_password(email_id,data['password'],data['confirmpassword'])
            responce_data.update({'success': True, 'data': [], 'message': "Password Reset successfull"})

            Response(self).jsonResponse(status=200, data=responce_data)

    def read_data(self):
        """
        This function is used for reading the data from the database.
        """
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST',
                     'CONTENT_TYPE': self.headers['Content-Type'],
                     })
        responce_data = {'success': True, 'data': [], 'message': ""}
        form_keys = list(form.keys())
        data = {'id': form['id'].value}
        data_base_object=DataBaseMangament()
        if len(form_keys) == 1:
            data_base_object.read(data)
            responce_data.update({'success': True, 'data': [], 'message': "Data read Successfully"})
            Response(self).jsonResponse(status=200, data=responce_data)
        else:
            responce_data.update({'success': False, 'data': [], 'message': "some values are missing"})
            Response(self).jsonResponse(status=404, data=responce_data)

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
            response_data = {'success': True, 'data': [], 'message': ""}
            data_base_object = DataBaseMangament()
            flag = data_base_object.validate_file_extension(profile_data)
            check = data_base_object.validate_file_size(profile_data)
            if flag and check:
                data_base_object.create_pic(profile_data)
                response_data.update({'success': True, "data": [], "message": "Profile Updated Successfully"})
                Response(self).jsonResponse(status=200, data=response_data)

            else:
                response_data .update({'success': True, "data": [], "message": "Unsupported file extension"})
                Response(self).jsonResponse(status=200, data=response_data)


    def is_trash(self):
        """
        This function is for reading data from the database according to Trash value.
        """
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST',
                     'CONTENT_TYPE': self.headers['Content-Type'],
                     })
        data = {'istrash': form['istrash'].value}
        responce_data = {'success': None, 'data': [], 'message': ""}
        data_base_object=DataBaseMangament()
        data_base_object.read_trash(data)
        responce_data.update({'success': True, 'data': [], 'message': "Data Read Successfully"})
        Response(self).jsonResponse(status=200, data=responce_data)



    def is_pinned(self):
        """
        This function is for reading data from the database according to Pinned value.
        """
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST',
                     'CONTENT_TYPE': self.headers['Content-Type'],
                     })
        responce_data = {'success': None, 'data': [], 'message': ""}
        data_base_object=DataBaseMangament()
        data = {'ispinned': form['ispinned'].value}

        data_base_object.read_pin(data)
        responce_data.update({'success': True, 'data': [], 'message': "Data Read Successfully"})
        Response(self).jsonResponse(status=200, data=responce_data)


    def is_archive(self):
        """
        This function is for reading data from the database according to Archive value.
        """
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST',
                     'CONTENT_TYPE': self.headers['Content-Type'],
                     })
        responce_data = {'success': None,'data':[],'message': ""}
        data_base_object=DataBaseMangament()
        data = {'isarchive': form['isarchive'].value}

        data_base_object.read_archive(data)
        responce_data.update({'success': True,'data':[], 'message': "Data Read Successfully"})
        Response(self).jsonResponse(status=200, data=responce_data)