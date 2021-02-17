from app import app
from helpers.mongoConnection import celebs_query, insert_celeb, remove_celeb, check_id_exists
from bson import json_util
from flask import request
from bson.objectid import ObjectId

from pymongo import MongoClient
client = MongoClient()
cel_db = client.lab_flask.celebrities

@app.route("/celebrities")
def get_celebrities():
    return json_util.dumps(celebs_query())

@app.route("/celebrities/details/<celeb_id>")
def get_cele_details(celeb_id):
    if check_id_exists(celeb_id):
        celeb = cel_db.find_one({'_id': ObjectId(str(celeb_id))}, {'_id':1, 'name':1, "occupation":1, "catch phrase":1})
        return json_util.dumps(celeb)
    else:
        return "Celeb_id does not exist"
        
@app.route("/celebrities/new/<name>/<occupation>/<catch_phrase>")
def add_celeb(name, occupation, catch_phrase):
    list_names = json_util.dumps(cel_db.find({}, {"_id":0, "name":1}))
    if name not in list_names:
        insert_celeb(name, occupation, catch_phrase)
        return json_util.dumps(celebs_query(name = name))
    else:
        return f"{name} is not available"

@app.route("/celebrities/delete/<celeb_id>")
def delete_celeb(celeb_id):
    if check_id_exists(celeb_id):
        remove_celeb(celeb_id)
        return f"{celeb_id} has been deleted"
    else:
        return f"Celeb_id {celeb_id} does not exist"
        
'''
@app.route("/celebrities/edit/<celeb_id>")
def edit_celeb(celeb_id):
    id_check = cel_db.find_one({'_id': ObjectId(str(celeb_id))})
    if check_id_exists(celeb_id):
        
    else:
        return "Celeb_id does not exist"
'''
