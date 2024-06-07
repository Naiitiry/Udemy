from flask import Flask, request,render_template,url_for,session
from werkzeug.utils import redirect
from werkzeug.exceptions import abort

app = Flask(__name__)

# Clase 536 - Sesiones
app.secret_key='Mi-llave_secreta!'

# http://localhost:5000/
@app.route("/")
def inicio():
    if 'username' in session:
        return f'<h2>El usuario {session["username"]} a hecho loggin</h2>'
    return "<h2>No ha hecho loggin!</h2>"

@app.route('/login',methods=['GET','POST'])
def loggin():
    if request.method == 'POST':
        # Omitimos la validación de usuario y password
        usuario = request.form['username']
        # Agregar usuario a la sesion
        session['username'] = usuario
        return redirect(url_for('inicio'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username')
    return redirect(url_for('inicio'))

@app.route("/saludar/<nombre>")
def saludo(nombre):
    return f"¡Bienvenido al Himalaya, {nombre}!"

@app.route("/edad/<int:edad>")
def mostrar_edad(edad):
    return f'Tu edad es: {edad}'

@app.route("/mostrar/<nombre>",methods=['GET','POST'])
def mostrar(nombre):
    return render_template('mostrar.html', nombre=nombre)

@app.route("/redireccionar")
def redireccionar():
    # para redirect se utiliza: from werkzeug.utils import redirect
    return redirect(url_for('inicio'))

# Clase 533 - Manejo de errores en Flask

@app.route('/salir')
def salir():
    # para abort se utiliza: from werkzeug.exceptions import abort
    return abort(404)

@app.errorhandler(404)
def pagina_no_encontrada(error):
    return render_template('error404.html',error=error),404

# Clase 534 - Uso de JSON y Flask

# REST -> REpresentation State Transfer

@app.route("/api/mostrar/<nombre>",methods=["GET","POST"])
def mostrar_json(nombre):
    valores = {'nombre':nombre,'metodo_http':request.method}
    return valores

# Ejecutar desde modo Desarrollo: 
# En windows
# set FLASK_APP=app.py
# set FLASK_ENV=development

# en linux/mac
# export FLASK_APP=app.py
# export FLASK_ENV=development

# en las versiones de 3.X se utiliza --debug al final

# flask run --debug