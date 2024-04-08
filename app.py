from flask import Flask, render_template, request, Response, jsonify, redirect, url_for
from controlador.auth import verificar_autenticacion
from flask_mongoengine import MongoEngine
from mongoengine import *
from config import MONGODB_SETTINGS

# from controlador.userController import verificar_autenticacion

app = Flask(__name__)
app.secret_key = 'LoQueYoDesee'

app.config.update(MONGODB_SETTINGS)

db = MongoEngine(app)


def connect_db():
    db.init_app(app)




from controlador.userController import *
from controlador.productsController import *


    


if __name__ == '__main__':
    app.run(debug=True, port=4000)