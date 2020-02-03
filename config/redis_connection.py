"""
@Author : P.Gnanender Reddy
@Since : Dec'2019
@Keywords:Redis database,.
@Description:This class is for Redis Data Base connection.
"""

import redis
from config.singleton import singleton
import os

@singleton
class RedisService:
    """
    Here we used singleton decorator for single object creation.This class is for redis database(cache memory).
    """
    def __init__(self, **kwargs):
        self.connection = self.connect(**kwargs)

    def connect(self, **kwargs):
        """
        This function is used for connecting the redis database.
        """
        redis_con = redis.StrictRedis(host=kwargs["host"], port=kwargs["port"])
        return redis_con

    def set(self, key, value):
        """
        This set function is used for setting the required value for required key.
        """
        self.connection.set(key, value)

    def get(self, key):
        """
        This get function is used for getting the value for appropriate key which is set by above set function.
        """
        print(key)
        value = self.connection.get(key)
        return value

    def disconnect(self):
        """
        This function is used for closing the connection.
        """
        self.connection.close()

con = RedisService(host=os.getenv('REDIS_HOST'),
    port=6379,

    )
