#!/usr/bin/env python3
""" python  script to insert many data into a collection """


def insert_school(mongo_collection, **kwargs):
    """ function that inserts new documents to the collection """
    mongo_collection.insert_one(kwargs)
    return mongo_collection.find({'_id' : kwargs['_id'] }, {'_id': 1})
