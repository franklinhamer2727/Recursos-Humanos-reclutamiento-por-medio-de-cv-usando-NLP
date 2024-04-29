from pymongo import MongoClient
import json
import os
from dotenv import load_dotenv

load_dotenv()
db_host = os.getenv("IP_CONEXION")
db_user = os.getenv("USUARIO_CONEXION")
db_pass = os.getenv("CONTRASENA_CONEXION")
db_name = os.getenv("DB_NAME")
col_collection = os.getenv("DB_COLLECTION")
col_collection_ = os.getenv("DB_COLLECTION_FILTRO")

def conexion_db(db_name):
    try:
        client = MongoClient(f"mongodb://{db_user}:{db_pass}@{db_host}")
        db = client[db_name]
        print("conexion exitosa!")
        return client, db
    except Exception as e:
        print(f"El conexion no es valido: {e}")
        return None,None

def conexion_collection(col_collection,db_name):
    client, db = conexion_db(db_name)
    collection = db[col_collection]
    return collection, db, client



