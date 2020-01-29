import redis
from config.singleton import singleton
import os

@singleton
class RedisService:
    def __init__(self, **kwargs):
        self.connection = self.connect(**kwargs)

    def connect(self, **kwargs):
        redis_con = redis.StrictRedis(host=kwargs["host"], port=kwargs["port"])
        return redis_con

    # password = kwargs["passwd"]

    def set(self, key, value):
        self.connection.set(key, value)

    def get(self, key):
        print(key)
        value = self.connection.get(key)
        return value

    def disconnect(self):
        self.connection.close()

con = RedisService(host=os.getenv('REDIS_HOST'),
    port=6379,
    # passwd='Password@123',
    )
# key ="hh"
# value = "gns"
# con.set(key,value)
# print(con.get(key))
# host='localhost'
