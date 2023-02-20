from . import db


def inserter(metadata):
    db.collection.insert_one(metadata)