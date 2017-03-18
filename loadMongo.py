from pymongo import MongoClient
import pickle
import Poetry

poems = list(pickle.load(open('poems_export.p', 'rb')))
poets = list(pickle.load(open('poets_export.p', 'rb')))

client = MongoClient()
db = client.explorer

for p in poems:
    p.categories = list(p.categories)
    db.poems.insert_one(p.__dict__)

for pt in poets:
    pt.categories = list(pt.categories)
    db.poets.insert_one(pt.__dict__)



