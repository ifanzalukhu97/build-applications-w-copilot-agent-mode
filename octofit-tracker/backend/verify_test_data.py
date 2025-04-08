from pymongo import MongoClient

# MongoDB connection details
client = MongoClient(host='localhost', port=27017)
db = client['octofit_db']

# Verify collections
collections = db.list_collection_names()
print("Collections in the database:", collections)

# Verify data in each collection
for collection in collections:
    data = list(db[collection].find())
    print(f"\nData in {collection}:")
    for item in data:
        print(item)
