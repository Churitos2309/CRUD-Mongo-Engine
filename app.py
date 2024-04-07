from flask import Flask, render_template, request, Response, jsonify, redirect, url_for
from controlador.auth import verificar_autenticacion
from flask_mongoengine import MongoEngine

# from controlador.userController import verificar_autenticacion

app = Flask(__name__)
app.secret_key = 'LoQueYoDesee'

db = MongoEngine(app)

def connect_db():
    app.config['MONGODB_SETTINGS'] = {
        'db': 'dbb_productos_app_mongoengine',
        'host': 'mongodb+srv://JuanOchoa:ANA2000JUAN@cluster0.cof4rpm.mongodb.net/dbb_productos_app_mongoengine?retryWrites=true&w=majority'
    }
    db.init_app(app)




from controlador.userController import *
from controlador.productsController import *


    


if __name__ == '__main__':
    app.run(debug=True, port=4000)