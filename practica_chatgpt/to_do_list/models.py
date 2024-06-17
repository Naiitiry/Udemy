from app import db
from datetime import datetime
import zoneinfo
from flask_login import UserMixin

# función de tiempo en UTC
def utcnow():
    return datetime.now(zoneinfo.ZoneInfo("UTC"))

class Usuario(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    nombre_usuario = db.Column(db.String(20),unique=True,nullable=False)
    password = db.Column(db.String(20),nullable=False)
    email = db.Column(db.String(120),unique=True,nullable=False)
    is_admin = db.Column(db.Boolean,default=False)
    tarea = db.relationship('Tareas',backref='author',lazy=True)

    def __repr__(self):
        return f'Bienvenido {self.nombre_usuario}'
    
class Tareas(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    titulo = db.Column(db.String(100),nullable=False)
    descripcion = db.Column(db.Text,nullable=False)
    fecha_publicado = db.Column(db.Datetime,nullable=False,default = utcnow)
    fecha_limite = db.Column(db.Datetime,nullable=False)
    user_id = db.Column(db.Integer,db.ForeingKey('user.id'),nullable=False)

    def __repr__(self):
        return f'Tareas: {self.title}, tiempo de finalización: {self.deadline}'