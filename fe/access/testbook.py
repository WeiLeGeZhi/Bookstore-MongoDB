import pymongo
db_path = "mongodb://localhost:27017"
db_name = "bookstore1"
client = pymongo.MongoClient(db_path)
db = client[db_name]
cursor = db.books.find({})
print(cursor[1].get("_id"))