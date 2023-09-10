from flask import Blueprint, render_template, request, redirect, url_for
from models.atses import Clientes
from utils.db import db

cliente = Blueprint("cliente", __name__)

# ELIMINAR, ACTUALIZAR Y CREAR CLIENTES:

@cliente.route("/clientes")
def clientes():
    clientes = Clientes.query.all()
    return render_template("clientes.html", clientes=clientes)


@cliente.route("/registrocliente")
def registrarcliente():
    return render_template("registrocliente.html")


@cliente.route("/registrocliente", methods=['POST'])
def registro_cliente():
    id_cliente = (request.form['id_cliente'])
    tipo_doc = (request.form['tipo_doc'])
    nombre = (request.form['nombre'])
    apellido = (request.form['apellido'])
    tipo_persona = (request.form['tipo_persona'])
    telefono = (request.form['telefono'])
    direccion = (request.form['direccion'])
    ciudad = (request.form['ciudad'])
    correo = (request.form['correo'])

    nuevo_cliente = Clientes(id_cliente, tipo_doc, nombre,apellido, tipo_persona, telefono, direccion, ciudad, correo)

    db.session.add(nuevo_cliente)
    db.session.commit()

    return redirect(url_for('cliente.clientes'))


@cliente.route("/actualizarcliente/<id_cliente>", methods=['POST','GET'])
def actualizar_cliente(id_cliente):
    if request.method == 'POST':
        cliente = Clientes.query.get(id_cliente)

        cliente.id_cliente = request.form['id_cliente']
        cliente.tipo_doc = request.form['tipo_doc']
        cliente.nombre = request.form['nombre']
        cliente.apellido = request.form['apellido']
        cliente.tipo_persona = request.form['tipo_persona']
        cliente.telefono = request.form['telefono']
        cliente.direccion = request.form['direccion']
        cliente.ciudad = request.form['ciudad']
        cliente.correo = request.form['correo']

        db.session.commit()
        return redirect(url_for('cliente.clientes'))
    
    cliente = Clientes.query.get(id_cliente)
    return render_template('/actualizarcliente.html', cliente=cliente)


@cliente.route("/eliminarcliente/<id_cliente>")
def eliminar_cliente(id_cliente):
    cliente = Clientes.query.get(id_cliente)
    db.session.delete(cliente)
    db.session.commit()
    return redirect(url_for('cliente.clientes'))
