# from  mongoengine import *
from flask import Flask
from flask_mongoengine import MongoEngine

app = Flask(__name__)

def connect_db(app):
    app.config['MONGODB_SETTINGS'] = {
        'db': 'dbb_productos_app_mongoengine',
        'host': 'mongodb+srv://JuanOchoa:ANA2000JUAN@cluster0.cof4rpm.mongodb.net/dbb_productos_app_mongoengine?retryWrites=true&w=majority'
    }
    db = MongoEngine(app)
    return db
    





# db = connect(host="mongodb+srv://JuanOchoa:ANA2000JUAN@cluster0.cof4rpm.mongodb.net/dbb_productos_app")



# from app import app
# from flask_mongoengine import MongoEngine

# app = app

# app.config['MONGODB_SETTINGS'] = {
#     'db': 'dbb_productos_app',
#     'host': 'mongodb+srv://JuanOchoa:ANA2000JUAN@cluster0.cof4rpm.mongodb.net/',
#     'port': 27017,
# }
# db = MongoEngine(app)






# from pymongo import MongoClient
# import certifi


# MONGO_URI = 'mongodb+srv://JuanOchoa:ANA2000JUAN@cluster0.cof4rpm.mongodb.net/'

# ca = certifi.where()

# def dbConnection():
#     try:
#         client = MongoClient(MONGO_URI, tlsCaFile=ca)
#         db = client["dbb_productos_app"]
        
#     except ConnectionError:
#         print("No se ha podido conectar con la base de datos")
    
#     return db