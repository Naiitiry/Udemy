from flask import Flask, render_template,redirect, url_for,request
from flask_migrate import Migrate
from database import db
from forms import PersonaForm


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

# Configuración de Flask-WTF
app.config['SECRET_KEY']='llave_secreta'

# Inicialización de objeto db de sqlalchemy
# esta en database.py
db.init_app(app)

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

#LAS CLASES ESTÁN EN models.py

# Agregamos acá la siguiente importación para que no provoque errores
# de circulación de importación con la db y la app.
from models import Persona

# Clase 543 - Listaado de Personas

@app.route('/')
@app.route('/index')
@app.route('/index.html')

def inicio():
    # Listado de personas
    # Ordenamos por columna
    personas = Persona.query.order_by('id')
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

# Ruta para agregar a la persona
@app.route('/agregar',methods=['GET','POST'])
def agregar():
    #para manejar los formularios con FLASK se utiliza WTF
    #por eso pasamos a instalarlo:
    # python -m pip install flask-wtf
    persona = Persona()
    personaForm = PersonaForm(obj=persona)
    if request.method == 'POST':
        if personaForm.validate_on_submit():
            personaForm.populate_obj(persona)
            app.logger.debug(f'Persona a insertar: {persona}')
            # Insertamos el nuevo registro
            db.session.add(persona)
            db.session.commit()
            return redirect(url_for('inicio'))
    return render_template('agregar.html',forma = personaForm)

# Editar un registro
@app.route('/editar/<int:id>',methods=['GET','POST'])
def editar(id):
    #Recuperamos el objeto Persona a editar
    persona=Persona.query.get_or_404(id)
    personaForma = PersonaForm(obj=persona)
    if request.method == 'POST':
        if personaForma.validate_on_submit():
            personaForma.populate_obj(persona)
            app.logger.debug(f'Persona a editar: {persona}')
            # Actualizamos los datos en la base de datos
            db.session.commit()
            return redirect(url_for('inicio'))
    return render_template('editar.html',forma=personaForma)

# Eliminar persona
@app.route('/eliminar/<int:id>')
def eliminar(id):
    persona = Persona.query.get_or_404(id)
    app.logger.debug(f'Persona a eliminar: {persona}')
    db.session.delete(persona)
    db.session.commit()
    return redirect(url_for('inicio'))

# en las versiones de 3.X se utiliza --debug al final
# flask run --debug.