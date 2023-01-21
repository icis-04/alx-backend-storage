#!/usr/bin/env python3
""" Scripts that update documents with a particular name """


def update_topics(mongo_collection, name, topics):
    """ function that updates a document in mongodb """
    query = { "name": name }
    updates = { "$set": { "topics": topics } }
    mongo_collection.update_many(query, updates)
