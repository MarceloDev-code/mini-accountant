from flask import Blueprint, request, render_template, redirect, url_for
from .models import db, Transaccion
from datetime import datetime

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    transacciones = Transaccion.query.order_by(Transaccion.fecha.desc()).all()
    ingresos = sum(t.monto for t in transacciones if t.tipo == 'ingreso')
    egresos = sum(t.monto for t in transacciones if t.tipo == 'egreso')
    saldo = ingresos - egresos
    return render_template('index.html', transacciones=transacciones, ingresos=ingresos, egresos=egresos, saldo=saldo)

@bp.route('/agregar', methods=['POST'])
def agregar():
    descripcion = request.form['descripcion']
    monto = float(request.form['monto'])
    tipo = request.form['tipo']
    fecha = datetime.strptime(request.form['fecha'], "%Y-%m-%d").date()

    nueva = Transaccion(descripcion=descripcion, monto=monto, tipo=tipo, fecha=fecha)
    db.session.add(nueva)
    db.session.commit()
    return redirect(url_for('main.index'))
