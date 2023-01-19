#!/usr/bin/env python3
""" Script that prints all the documents in a collection """


def list_all(mongo_collection):
    """ function that lists all documents in a collection
    if len(list(mongo_collection)) == 0:
        return [] """
    return mongo_collection.list_collection_names()
