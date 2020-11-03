import pymongo
from pymongo import MongoClient
import os
def connessione():
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

    file=open(os.path.join(__location__, "MongoDB configurazione.txt" ),"r")
    url=file.readline().replace("link=",'').rstrip("\n")
    database=file.readline().replace("database=",'').rstrip("\n")
    collezione=file.readline().replace("collection=",'').rstrip("\n")
    cluster = MongoClient(url)
    db=cluster[database]
    collection=db[collezione]
    file.close()
    return collection

