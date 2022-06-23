from pymongo import MongoClient
import certifi
url="mongodb+srv://admin:admin@cluster0.3f0yk.mongodb.net/?retryWrites=true&w=majority"
client=MongoClient(url,tlsCAFile=certifi.where())
db=client.pytech
print("--pytech Collection List--\n",
db.list_collection_names())
input("Program has finished, please press Enter to exit...")