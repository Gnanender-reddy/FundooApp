import jwt

from config.redis_connection import RedisService
from models.datamanagement import DataBaseMangament
from view.response import Response
from view.utils import Utility
from datetime import datetime, timedelta
from auth.login_authentication import response
JWT_SECRET = 'secret'
JWT_ALGORITHM = 'HS256'
JWT_EXP_DELTA_SECONDS = 100000000


class user:
    def register(self,data):
        data_base_object = DataBaseMangament()
        util = Utility()
        responce={'success':True,'data':[],'message':""}

        if util.password_validation(data) and util.email_validation(data['email']):
            data_base_object.registration(data)
            responce.update({'success': True, 'data': [], 'message': "Successfully registered"})
            return responce
        else:
             responce.update({'success':False,'data':[],'message':"not registered"})
             return responce

    def login(self,data):
        data_base_object=DataBaseMangament()
        email = data['email']
        id, email = data_base_object.read_email(email=email)
        responce={'success':True,'data':[],'message':"",'data':''}

        if id:
            payload = {'id': id, 'exp': datetime.utcnow() + timedelta(seconds=JWT_EXP_DELTA_SECONDS)}
            encoded_token = jwt.encode(payload, 'secret', 'HS256').decode('utf-8')
            print(id, encoded_token)
            redis_obj = RedisService()
            redis_obj.set(id, encoded_token)
            print(redis_obj.get(id), '------------->r.get')
            responce.update({'success': True, 'data': [], 'message': "Successfully login","token": encoded_token})
            return responce
