from flask import Flask, render_template, redirect, url_for, request, session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mongoengine import MongoEngine
from mongoengine import *
from app import app,db
from database import connect_db

app = Flask(__name__)
connection = connect_db(app, alias='aliasconnect_db')


# Definición del modelo de usuario
class Usuario(Document):
    username = StringField(max_length=50, unique=True)
    password = StringField(max_length=100)
    correo = StringField(max_length=100)

    def __str__(self):
        return self.username
@app.route('/register', methods=['GET', 'POST'])
def register():
    mensaje_error = None

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        correo = request.form['correo']

        # Verifica si el usuario ya existe en la base de datos
        existe_user = Usuario.objects(username=username).first()
        if existe_user is None:
            # Inserta el nuevo usuario en la base de datos
            usuario = Usuario(username=username, password=generate_password_hash(password), correo=correo)
            usuario.save()
            return redirect(url_for('login'))
        else:
            mensaje_error = 'Usuario ya existe. Intenta con otro nombre de usuario'

    return render_template('register.html', mensaje_error=mensaje_error)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Busca al usuario en la base de datos por nombre de usuario y contraseña
        user = Usuario.objects(username=username, password=generate_password_hash(password)).first()
        if user:
            session['username'] = username
            return redirect(url_for('index'))
        else:
            return 'Credenciales incorrectas. Intenta nuevamente'

@app.route('/ensayo')
def ensayo():
    if 'username' in session:
        return 'hola' + session['username']
    return redirect(url_for('login'))

@app.route('/')
def index():
    if 'username' in session:
        return 'hola' + session['username']
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)




















































# from app import app,db,verificar_autenticacion  # Importa la instancia de la aplicación Flask desde el archivo app.py
# from flask import Flask, request, redirect, url_for, render_template, session  # Importa las clases y funciones necesarias de Flask
# from bson import ObjectId  # Importa ObjectId de la biblioteca bson
# from functools import wraps  # Importa wraps desde functools para los decoradores
# from database import connect_db # Importa el modulo database como dbase

# # Establece la conexion a la base de datos
# # db = dbase.dbConnection()
# db = connect_db()
# usuarios_coleccion = db.usuarios  # Obtiene la coleccion de usuarios



# @app.route('/register', methods=['GET', 'POST'])
# @verificar_autenticacion# Ruta para registrar nuevos usuarios
# def register():
#     mensaje_error = None  # Mensaje de error inicialmente vacio
    
#     if request.method == 'POST':  # Si se envia un formulario
#         username = request.form['username']  # Obtiene el nombre de usuario del formulario
#         password = request.form['password']  # Obtiene la contraseña del formulario
#         correo = request.form['correo']  # Obtiene el correo electronico del formulario
        
#         # Verifica si el usuario ya existe en la base de datos
#         existe_user = usuarios_coleccion.find_one({'username': username})
#         if existe_user is None:  # Si el usuario no existe
#             # Inserta el nuevo usuario en la base de datos
#             usuarios_coleccion.insert_one({'username': username, 'password': password, 'correo': correo})        
#             return redirect(url_for('login'))  # Redirige al usuario a la pagina de inicio de sesion
#         else:
#             mensaje_error = 'Credenciales incorrectas. Intenta nuevamente'  # Establece el mensaje de error
    
#     # Renderiza el template de registro, pasando el mensaje de error
#     return render_template('login.html', mensaje_error=mensaje_error)

# # Ruta para el inicio de sesion

# @app.route('/login', methods=['GET', 'POST'])
# @verificar_autenticacion# Ruta para registrar nuevos usuarios
# def login():
#     if request.method == 'POST':  # Si se envia un formulario de inicio de sesion
#         username = request.form['username']  # Obtiene el nombre de usuario del formulario
#         password = request.form['password']  # Obtiene la contraseña del formulario
        
#         # Busca al usuario en la base de datos por nombre de usuario y contraseña
#         user = usuarios_coleccion.find_one({'username': username, 'password': password})
#         if user:  # Si se encontro un usuario con las credenciales proporcionadas
#             session['username'] = username  # Establece la sesion con el nombre de usuario
#             return redirect(url_for('index'))  # Redirige al usuario a la pagina principal
#         else:
#             return 'Credenciales incorrectas. Intenta nuevamente'  # Mensaje de error si las credenciales son incorrectas
    
#     # Renderiza el template de inicio de sesion
#     return render_template('login.html')

# # Ruta para la pagina de ensayo (requiere autenticacion)
# @app.route('/ensayo')
# @verificar_autenticacion
# def ensayo():
#     return render_template('ensayo.html')  # Renderiza el template de ensayo

# # Ruta para la página principal (requiere autenticación)
# @app.route('/')
# @verificar_autenticacion
# def index():
#     if 'username' in session:  # Si el usuario está autenticado
#         return 'hola' +  session['username']  # Saluda al usuario
#     return redirect(url_for('login'))  # Redirige al usuario a la página de inicio de sesión si no está autenticado

# # Ruta para cerrar sesión

# @app.route('/logout')
# @verificar_autenticacion
# def logout():
#     session.pop('username', None)  # Elimina el nombre de usuario de la sesión
#     return redirect(url_for('login'))  # Redirige al usuario a la página de inicio de sesión
