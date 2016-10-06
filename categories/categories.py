from pymongo import MongoClient
from bson.json_util import dumps


def categories_handler(event, context):
    client = MongoClient('localhost', 27017)
    db = client['grain']
    collection = db['categories']

    r = collection.find()
    l = list(r)

    return dumps(l)
