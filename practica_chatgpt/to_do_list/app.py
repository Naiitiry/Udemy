from flask import Flask,render_template,redirect,url_for,request,flash,abort
from flask_migrate import Migrate
from flask_login import current_user, login_user, logout_user,login_required
from database import db
from forms import RegistroFormulario, Login,Tareas
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)

# ************* Configuración de BD *************
USER_DB = 'postgres'
PASS_DB = 'admin'
URL_DB = 'localhost'
NAME_DB = 'to_do_list'
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

from models import Usuario,Tareas

# *************** Registro, login y logout ***************

# Ruta de registro
@app.route('/registro',methods=['POST','GET'])
def registro():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistroFormulario()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.contrasenia.data)
        user = Usuario(username=form.nombre_usuario.data,email=form.email.data,password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Tu cuenta fue creada!','success')
        return redirect(url_for('login'))
    return render_template('registro.html',title='Registro',form=form)

# Ruta de login
@app.route('/login',methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = Login()
    if form.validate_on_submit():
        user = Usuario.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password,form.contrasenia.data):
            login_user(user, remember=form.recordar.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('index'))
        else:
            flash('Loggeo insatisfactorio. Por favor, revise su E-mail y contraseña','danger')
    return render_template('login.html',title='Login',form=form)


# Ruta de logout
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


# *************** TAREAS ***************

@app.route('/task/new',method=['GET','POST'])
def new_task():
    form = Tareas()
    if form.validate_on_submit():
        task = Tareas(title=form.titulo.data,description=form.descripcion.data,deadline=form.fecha_limite.data,author=current_user)
        db.session.add(task)
        db.session.commit()
        flash('Tu tarea fue creada con éxito','success')
        return redirect(url_for('index'))
    return render_template('crear_tarea.html',title='nueva tarea',form=form)


# Buscamos una tarea por el ID con la condición de que tengo que estar logeado
@app.route('/task/<int:id>')
# Aplicamos el decorador que necesita estar login
@login_required
def tarea(id):
    task = Tareas.query.get_or_404(id)
    return render_template('tarea.html',title='Tarea',task=task)


# Buscamos una tarea por el ID con la condición de que tengo que estar logeado
# y poder modificar la misma
@app.route('/task/<int:id>/update',methods=['GET','POST'])
# Aplicamos el decorador que necesita estar login
@login_required 
def update_task(id):
    task = Tareas.query.get_or_404(id)
    if task.author != current_user:
        abort(403)
    form = Tareas()
    if form.validate_on_submit():
        task.title = form.titulo.data
        task.desciption = form.descripcion.data
        task.deadline = form.fecha_limite.data
        db.session.commit()
        flash('Tus cambios fueron realizado con éxito.','success')
        return redirect(url_for('tarea',id=task.id))
    elif request.method == 'GET':
        form.titulo.data = task.title
        form.descripcion.data = task.description
        form.fecha_limite.data = task.deadline
    return render_template('crear_tarea.html',title='Actualizar tarea',form=form)


# Eliminar una tarea
@app.route('/task/<int:id>/delete',methods=['POST'])
@login_required
def delete_task(id):
    task = Tareas.query.get_or_404(id)
    if task.author != current_user:
        abort(403)
    db.session.delete(task)
    db.session.commit()
    flash('Tu tarea fue eliminada exitosamente','success')
    return redirect(url_for('index'))



# *************** INDEX ***************

@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index():
    return '<h1>Bienvenido al Himalaya!</h1>'


# Hacer correr en modo debug
# flask run --debug