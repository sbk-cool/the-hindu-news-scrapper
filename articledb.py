import pymongo as pym
import datetime as dt

class ArticleDb:
    """Objective : Manage the articles collection.
    Function:
        1. Create Database if it does not exist.
        2. Create and manage article collection.
        3. Maintain connection to database's collection.
        4. Insert documents into collection.
    """
# Initialises MongoClient with host.
# Host is type str and port is type int.
    def __init__(self,host,port):
        self.host=host
        self.port=port
        self.client=pym.MongoClient(host,port)
        self.db=None
        self.collection=None
        self.db_name=''
        self.collection_name=''

# Initialise database and collection.
# db and collection both type str.
    def init_backend(self,db,collection):
        self.db_name=db
        self.collection_name=collection
        self.db=self.client[self.db_name]
        self.collection=self.db[self.collection_name]

# Inserts document to collection.
# This document is itself a list of the articles.
# Each article is string type.
    def insert_doc(self,document):
        doc={
                "date":dt.datetime.utcnow(),
                "articles":document
            }
        self.collection.insert_one(doc)
