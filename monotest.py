import pymongo

client = pymongo.MongoClient("mongodb+srv://ajay0305:D0305Ajay@cluster0.ieg8x.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)
