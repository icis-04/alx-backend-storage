#!/usr/bin/env python3
""" Script to communicate with redis server """
import redis 
import uuid
from typing import Any


class Cache:
    """ class that initializes the redis server """


    def __init__(self) -> None:
        """ initializes the database """
        _redis = redis.Redis()
        _redis.flushdb()

    def store(data: Any) -> str:
        """ stores in a redis database """
        rand: uuid.uuid1() = uuid.uuid1()
        r.sadd(rand, *data)
        return str(rand)
