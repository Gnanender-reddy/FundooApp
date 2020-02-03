import jwt
from config.redis_connection import RedisService
from models.db_operations import Models
from vendor.smtp_connection import smtp
from view.utils import Utility
from datetime import datetime, timedelta
from auth.login_authentication import response
JWT_SECRET = 'secret'
JWT_ALGORITHM = 'HS256'
JWT_EXP_DELTA_SECONDS = 100000000


class UserServices:
    def __init__(self):
        self.data_base_object = Models()
        self.util=Utility()

    def register(self,data):


        if self.data_base_object.checking_email(data['email']):
            res=response(message="entered email already registered")
            return res
        else:
            if self.util.password_validation(data) and self.util.email_validation(data['email']):
                data={'email':data['email'],'password':data['password']}
                self.data_base_object.user_insert(data,table_name='users')
                res = response(success=True,message="Successfully registered")
                return res
            else:
                res = response(message="Please enter your credentials in proper format")
                return res





    def login(self,data):

        email = data['email']
        responce = {'success': True, 'data': [], 'message': "", 'data': ''}
        if self.data_base_object.checking_email(email):
            id, email = self.data_base_object.read_email(email=email)
            if id :
                payload = {'id': id, 'exp': datetime.utcnow() + timedelta(seconds=JWT_EXP_DELTA_SECONDS)}
                encoded_token = jwt.encode(payload, 'secret', 'HS256').decode('utf-8')
                print(id, encoded_token)
                redis_obj = RedisService()
                redis_obj.set(id, encoded_token)
                print(redis_obj.get(id), '------------->r.get')
                responce.update({'success': True, 'data': [], 'message': "Successfully login","token": encoded_token})
                return responce
        else:
            res = response(message="Login unsuccessfull")
            return res

    def forgot(self,data,version,host):

        if self.data_base_object.checkinguser(data['email']):
            email = data['email']
            s = smtp()
            encoded_jwt = jwt.encode({'email': email}, 'secret', algorithm='HS256').decode("UTF-8")
            data = f"{host}://{version}/reset/?new={encoded_jwt}"
            s.send_mail(email, data)
            res = response(success=True, message="Message sent successfully")
            return res
        else:
            res = response(message="unsuccessfull")
            return res

    def reset_password(self,form_keys,data,email_id):

        if len(form_keys) < 2:
            res = response(message="some values are missing")
            return res
        else:

            self.data_base_object.update_password(email_id,data['password'])
            res = response(success=True, message="Password Reset successfull")
            return res



    def profile_picture(self,profile_data):

        flag = self.util.validate_file_extension(profile_data)
        check = self.util.validate_file_size(profile_data)
        if flag and check:
            self.data_base_object.create_pic(profile_data)
            res = response(success=True, message="Profile Updated Successfully")
            return res
        else:
            res = response(message="Unsupported file extension")
            return res






