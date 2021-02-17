from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient()

cel_db = client.lab_flask.celebrities

def celebs_query(**kwargs):
    '''
    makes quueries to the celebrities collection

    Takes: values to be queried
    Returns: list with matching celebrities with their occupation and catch phrase
    '''
    res = cel_db.find(kwargs,{"_id":1, "name":1})
    return list(res)

def insert_celeb(name, occupation, catch_phrase):
    '''
    inserts a new celebrity in celebrities collection

    Takes: data to be inserted (name, occupation, catch phrase)
    Returns: nothing
    '''
    my_dict = {"name": name, "occupation": occupation, "catch phrase": catch_phrase}
    cel_db.insert_one(my_dict)

def remove_celeb(celeb_id):
    '''
    given an ID, removes a celebrity from the database

    Takes: _id
    Returns: nothing
    '''
    my_dict = {'_id': ObjectId(str(celeb_id))}
    cel_db.delete_one(my_dict)

'''
def change_celeb(celeb_id):
'''

def check_id_exists(celeb_id):
    id_check = cel_db.find_one({'_id': ObjectId(str(celeb_id))})
    if id_check is None:
        return False
    else:
        return True
