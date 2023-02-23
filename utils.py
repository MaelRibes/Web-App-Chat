from pymongo import MongoClient
def get_db_handle():
    client = MongoClient('mongodb+srv://Baki:joaquim2000@webchat.ydkwtjl.mongodb.net/test')
    db = client['WebChat']
    return db, client