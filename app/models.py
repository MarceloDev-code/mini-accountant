from flask_sqlalchemy import SQLAlchemy
from datetime import date

db = SQLAlchemy()

class Transaccion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(200), nullable=False)
    monto = db.Column(db.Float, nullable=False)
    tipo = db.Column(db.String(10), nullable=False)  # ingreso / egreso
    fecha = db.Column(db.Date, default=date.today)
