#!/usr/bin/env python3
""" python  script to insert many data into a collection """


def insert_school(mongo_collection, **kwargs):
    mongo_collection.insert_one(kwargs)
    return mongo_collection.find({'_id' : kwargs.get('_id')}, {'_id': 1})
