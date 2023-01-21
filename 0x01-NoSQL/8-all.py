#!/usr/bin/env python3
""" Script that prints all the documents in a collection """


def list_all(mongo_collection):
    """ function that lists all documents in a collection """
    if mongo_collection.find() == None:
        return []
    else:
        return mongo_collection.find()
