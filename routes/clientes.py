from flask import Blueprint, render_template, request, redirect
from models.atses import Clientes
from utils.db import db

atses = Blueprint("atses", __name__)


@atses.route("/")
def home():
    return render_template("index.html")


# ELIMINAR, ACTUALIZAR Y CREAR CLIENTES:


@atses.route("/clientes")
def clientes():
    clientes = Clientes.query.all()
    return render_template("clientes.html", clientes=clientes)


@atses.route("/registrocliente")
def registrarcliente():
    return render_template("registrocliente.html")


@atses.route("/nuevo", methods=['POST'])
def nuevo_cliente():
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
    print(nuevo_cliente)

    db.session.add(nuevo_cliente)
    db.session.commit()

    return redirect ('/clientes')


@atses.route("/actualizarcliente")
def actualizarcliente():
    return render_template("actualizarcliente.html")


@atses.route("/actualizar")
def actualizar_cliente():
    return "actualizado con exito"


@atses.route("/eliminar/<id_cliente>")
def eliminar_cliente(id_cliente):
    cliente = Clientes.query.get(id_cliente)
    db.session.delete(cliente)
    db.session.commit()
    return redirect('/clientes')
