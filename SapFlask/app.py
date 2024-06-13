from flask import Flask, render_template
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
    
# Clase 543 - Listaado de Personas

@app.route('/')
@app.route('/index')
@app.route('/index.html')

def inicio():
    # Listado de personas
    personas = Persona.query.all()
    total_personas = Persona.query.count()
    app.logger.debug(f'Listado Personas: {personas}')
    app.logger.debug(f'Total Personas: {total_personas}')
    return render_template('index.html',personas=personas,total_personas=total_personas)

# Buscamos a la persona por ID
@app.route('/ver/<int:id>')

# Definimos el método:
def ver_detalle(id):
    #Recuperamos la persona según el ID proporcionado.
    #persona = Persona.query.get(id)
    persona = Persona.query.get_or_404(id)
    # Se pone get_or_404 porque si no hay nada en esa ID
    # da el error 404, es para el manejo de errores.
    app.logger.debug(f'Listado persona: {persona}')
    return render_template('detalle.html',persona=persona)


# en las versiones de 3.X se utiliza --debug al final
# flask run --debug.