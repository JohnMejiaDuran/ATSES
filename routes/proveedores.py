from flask import Blueprint, render_template, request, redirect, url_for
from models.atses import Proveedores
from utils.db import db

proveedor = Blueprint("proveedor", __name__)

@proveedor.route("/proveedores")
def proveedores():
    proveedores = Proveedores.query.all()
    return render_template("proveedores.html", proveedores=proveedores)

@proveedor.route("/registroproveedor")
def registrarproveedor():
    return render_template("registroproveedor.html")

@proveedor.route("/registroproveedor", methods=['POST'])
def registro_proveedor():
    id_proveedor = (request.form['id_proveedor'])
    nombre = (request.form['nombre'])
    telefono = (request.form['telefono'])
    direccion = (request.form['direccion'])
    ciudad = (request.form['ciudad'])
    correo = (request.form['correo'])

    nuevo_proveedor = Proveedores(id_proveedor, nombre, telefono, direccion, ciudad, correo)

    db.session.add(nuevo_proveedor)
    db.session.commit()

    return redirect(url_for('proveedor.proveedores'))

@proveedor.route("/actualizarproveedor/<id_proveedor>", methods=['POST','GET'])
def actualizar_proveedor(id_proveedor):
    if request.method == 'POST':
        proveedor = Proveedores.query.get(id_proveedor)
        proveedor.id_proveedor = request.form['id_proveedor']
        proveedor.nombre = request.form['nombre']
        proveedor.telefono = request.form['telefono']
        proveedor.direccion = request.form['direccion']
        proveedor.ciudad = request.form['ciudad']
        proveedor.correo = request.form['correo']

        db.session.commit()
        return redirect(url_for('proveedor.proveedores'))
    
    proveedor = Proveedores.query.get(id_proveedor)
    return render_template('actualizarproveedor.html', proveedor=proveedor)

@proveedor.route("/eliminarproveedor/<id_proveedor>")
def eliminar_proveedor(id_proveedor):
    proveedor = Proveedores.query.get(id_proveedor)
    db.session.delete(proveedor)
    db.session.commit()
    return redirect(url_for('proveedor.proveedores'))