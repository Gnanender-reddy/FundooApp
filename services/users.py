import jwt
from config.redis_connection import RedisService
from models.datamanagement import DataBaseMangament
from vendor.smtp import smtp
from view.utils import Utility
from datetime import datetime, timedelta
from auth.login_authentication import response
JWT_SECRET = 'secret'
JWT_ALGORITHM = 'HS256'
JWT_EXP_DELTA_SECONDS = 100000000

# def response(success=False, message='something went wrong', data=[]):
#     response = {'success': success,
#     "message": message,
#     "data": data, }
#     return response
# res = response(message="Signature expired. Please log in again.")
#                 Response(self).jsonResponse(status=404, data=res)
class user:
    def __init__(self):
        self.data_base_object = DataBaseMangament()

    def register(self,data):

        util = Utility()
        if self.data_base_object.checking_email(data['email']):
            res=response(message="entered email already registered")
            return res
        else:
            if util.password_validation(data) and util.email_validation(data['email']):
                self.data_base_object.registration(data)
                res = response(success=True,message="Successfully registered")
                return res
            else:
                res = response(success=False, message="Please enter your credentials in proper format")
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
            res = response(success=False, message="Login unsuccessfull")
            return res

    def forgot(self,data,version,host):

        if self.data_base_object.checkinguser(data['email']):
            email = data['email']
            s = smtp()
            encoded_jwt = jwt.encode({'email': email}, 'secret', algorithm='HS256').decode("UTF-8")
            data = f"{version}://{host}/reset/?new={encoded_jwt}"
            s.send_mail(email, data)
            res = response(success=True, message="Message sent successfully")
            return res
        else:
            res = response(success=False, message="unsuccessfull")
            return res




