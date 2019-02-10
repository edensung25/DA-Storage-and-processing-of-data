import pymongo
from bson.son import SON
import pprint

client = pymongo.MongoClient()
db = client.DA
result = db.ratings.aggregate([{"$group" : {"_id" : "$movie_id", "avg_rating" : {"$avg" : "$rating"}}}])
print(list(result))
