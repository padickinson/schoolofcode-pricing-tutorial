import os

import pymongo

__author__ = 'padickinson'


class Database(object):
    # static class properties
    URI = os.environ.get("MONGODB_URI")
    # mongodb://<dbuser>:<dbpassword>@ds143340.mlab.com:43340/heroku_b8cxdkz8
    DATABASE = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client.get_default_database()
        #Database.DATABASE = client['heroku_b8cxdkz8']

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)

    @staticmethod
    def update(collection, query, data):
        Database.DATABASE[collection].update(query,data,upsert=True)

    @staticmethod
    def delete_one(collection,query):
        Database.DATABASE[collection].delete_one(query)

    @staticmethod
    def remove(collection, query):
        Database.DATABASE[collection].remove(query)