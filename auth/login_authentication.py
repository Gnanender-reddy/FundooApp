import jwt
from view.response import Response
from config.redis_connection import RedisService

#
def response(success=False, message='something went wrong', data=[]):
    response = {'success': success,
    "message": message,
    "data": data, }
    return response

def is_authenticated(method):
    def authenticate_user(self):
        try:
            print(self.path, type(self.path))
            if self.path in ['/note/api/createdata', '/api/note/delete', '/api/note/update','api/note/read', '/api/profile']:

                token = self.headers['token']
                print(token)
                payload = jwt.decode(token, "secret", algorithms='HS256')
                print(payload)
                id_key = payload['id']
                print(id_key)
                redis_obj = RedisService()
                token = redis_obj.get(id_key)
                print(token, '------->token')
                if token is None:
                    raise ValueError("You Need To Login First")
                return method(self)
            else:
                return method(self)
        except jwt.ExpiredSignatureError:
                res = response(message="Signature expired. Please log in again.")
                Response(self).jsonResponse(status=404, data=res)
        except jwt.DecodeError:
                res = response(message="DecodeError")
                Response(self).jsonResponse(status=404, data=res)
        except jwt.InvalidTokenError:
                res = response(message="InvalidTokenError")
                Response(self).jsonResponse(status=404, data=res)
    return authenticate_user
