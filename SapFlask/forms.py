from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

class PersonaForm(FlaskForm):
    # Creamos los Labels para el formulario
    nombre = StringField('Nombre',validators=[DataRequired()])
    apellido = StringField('Apellido')
    email = StringField('E-mail',validators=[DataRequired()])
    #Es opcional, pero podemos agregar los botones
    enviar = SubmitField('Enviar')