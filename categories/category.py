from pymongo import MongoClient
from pymongo import errors
from bson.json_util import dumps


def category_handler(event, context):
    try:
        client = MongoClient('localhost', 27017)
        db = client['grain']
        collection = db['categories']

        r = collection.find()
        l = list(r)

        return dumps(l)
    except errors.ConnectionFailure, e:
        return "Cannot connect to database host: %s" % e
    except errors.CollectionInvalid, e:
        return "Invalid collection: %s" % e