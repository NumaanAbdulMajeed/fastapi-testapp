from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import urllib

user_name = "numaanmajeed01"
passsword = "numaan@2003"
uri = "mongodb+srv://" + urllib.parse.quote(user_name)+":"+urllib.parse.quote(passsword)+ "@cluster0.re0zlye.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"


client = MongoClient(uri, server_api=ServerApi('1'))

db=client.todo_db
collection_name=db ["todo_collection"]


