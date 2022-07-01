import pymongo

client = pymongo.MongoClient("mongodb+srv://admin:admin@cluster0.ynpyc9f.mongodb.net/?retryWrites=true&w=majority")

#db = client['sample_airbnb']
#mydb = client["mydatabase"]
print("list_database_names: ", client.list_database_names())

#print("list_collection_names: ", db.list_collection_names())