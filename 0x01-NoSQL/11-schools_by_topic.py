#!/usr/bin/env python3
""" script to search for schools by topic """


def schools_by_topic(mongo_collection, topic):
    """function that returns collection by topics """
    return mongo_collection.find({ 'topics': topic })
