from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, DateTimeField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from models import Usuario
from flask_wtf import FlaskForm

class RegistroFormulario(FlaskForm):
    nombre_usuario = StringField('Usuario',validators=[DataRequired(),Length(min=2,max=20)])
    contrasenia = PasswordField('Contraseña',validators=[DataRequired(),])
    confirmar_contraseña = PasswordField('Confirmar contraseña',validators=[DataRequired(),EqualTo('contrasenia')])
    email = StringField('E-mail',validators=[DataRequired(),Email()])
    enviar = SubmitField('Registrar')

    def validar_usuario(self,nombre_usuario):
        user = Usuario.query.filter_by(nombre_usuario=nombre_usuario.data).first()
        if user:
            raise ValidationError('El usuario ya está siendo utilizado, por favor elija otro.')
        
    def validar_email(self,email):
        email = Usuario.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError('El E-mail, proporcionado, ya está en uso, por favor elija otro.')

class Login(FlaskForm):
    email = StringField('E-mail',validators=[DataRequired(),Email()])
    contrasenia = PasswordField('Contraseña',validators=[DataRequired()])
    recordar = BooleanField('Recordarme')
    enviar = SubmitField('Logearme')

class Tareas(FlaskForm):
    titulo = StringField('Título',validators=[DataRequired()])
    descripcion = TextAreaField('Descripción',validators=[DataRequired()])
    fecha_limite = DateTimeField('Fecha límite',validators=[DataRequired()])
    enviar = SubmitField('Agregar tarea')