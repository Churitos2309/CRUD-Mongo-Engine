from mongoengine import *

class Usuaio(Document):
    username = StringField(required=True, unique=True)
    password = StringField(required=True)
    correo = EmailField(required=True)
    
class Categoria(Document):
    nombre = StringField(required=True, unique=True)
    
class Product(Document):
    codigo = IntField(required=True, unique=True)
    nombre = StringField(required=True)
    precio = IntField(required=True)
    categoria = ReferenceField(Categoria)