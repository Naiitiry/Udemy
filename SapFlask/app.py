from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)

# ************* Configuración de BD *************
USER_DB = 'postgres'
PASS_DB = 'admin'
URL_DB = 'localhost'
NAME_DB = 'sap_flask_db'
# Cadena completa de conexión a POSTGRES
FULL_URL_DB = f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'

app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicialización de objeto db de sqlalchemy
db = SQLAlchemy(app)

# Configuración de Flask-migrate

migrate = Migrate()
migrate.init_app(app, db)

# Una vez creado primero la app, la db y la Clase con la herencia de db.Model
# ejecutamos "flask db init"
# luego ejecutamos "flask db migrate"
# y luego "flask db upgrade" para hacer el commit en la tablas de PostgresSQL.

# si hay cambios y/o actualización se debe ejecutar:
# "flask db stamp head"

# Ahí ejecutamos los 2 comandos anteriores ("flask db migrate" y "flask db upgrade") 
# para actualizar tabla/s

class Persona(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(250))
    apellido = db.Column(db.String(250))
    email = db.Column(db.String(250))

    def __str__(self):
        return (
            f'Id: {self.id}, '
            f'Nombre: {self.nombre}, '
            f'Apellidp: {self.apellido}, '
            f'Email: {self.email}'
        )