from flask import Blueprint, render_template

atses = Blueprint("atses", __name__)


@atses.route("/")
def home():
    return render_template('index.html')

# ELIMINAR, ACTUALIZAR Y CREAR CLIENTES:

@atses.route('/clientes')
def clientes():
    return render_template('clientes.html')

@atses.route('/actualizarcliente')
def actualizarcliente():
    return render_template('actualizarcliente.html')

@atses.route('/nuevo')
def nuevo_cliente():
    return "Agregado con exito"

@atses.route('/actualizar')
def actualizar_cliente():
    return "actualizado con exito"

@atses.route('/eliminar')
def eliminar_cliente():
    return "eliminado con exito"