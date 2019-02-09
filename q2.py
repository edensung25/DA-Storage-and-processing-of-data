import pymongo
from bson.son import SON
import pprint

client = pymongo.MongoClient()
db = client.DA
user_id = int(input())
movie_list = db.ratings.distinct("movie_id", {"user_id":user_id})
result = db.ratings.distinct("user_id", {"movie_id":{"$in":movie_list}})
print(result)
