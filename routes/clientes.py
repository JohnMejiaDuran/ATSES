from flask import Blueprint, render_template, request, redirect, url_for
from models.atses import Clientes
from utils.db import db

# Creación del Blueprint para Clientes
cliente = Blueprint("cliente", __name__)

# Ruta para mostrar la lista de clientes
@cliente.route("/clientes")
def clientes():
    # Recupera todos los clientes de la base de datos
    clientes = Clientes.query.all()
    # Renderiza la plantilla "clientes.html" y pasa la lista de clientes como contexto
    return render_template("clientes.html", clientes=clientes)

# Ruta para mostrar el formulario de registro de clientes
@cliente.route("/registrocliente")
def registrarcliente():
    # Renderiza la plantilla "registrocliente.html" para registrar nuevos clientes
    return render_template("registrocliente.html")

# Ruta para procesar el formulario de registro de clientes
@cliente.route("/registrocliente", methods=['POST'])
def registro_cliente():
    # Recupera los datos del formulario
    id_cliente = request.form['id_cliente']
    tipo_doc = request.form['tipo_doc']
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    tipo_persona = request.form['tipo_persona']
    telefono = request.form['telefono']
    direccion = request.form['direccion']
    ciudad = request.form['ciudad']
    correo = request.form['correo']

    # Crea un nuevo objeto Clientes con los datos del formulario
    nuevo_cliente = Clientes(id_cliente, tipo_doc, nombre, apellido, tipo_persona, telefono, direccion, ciudad, correo)

    # Agrega el nuevo cliente a la sesión de la base de datos
    db.session.add(nuevo_cliente)
    # Confirma los cambios en la base de datos
    db.session.commit()

    # Redirige a la página de lista de clientes después de registrar uno nuevo
    return redirect(url_for('cliente.clientes'))

# Ruta para actualizar un cliente específico
@cliente.route("/actualizarcliente/<id_cliente>", methods=['POST','GET'])
def actualizar_cliente(id_cliente):
    if request.method == 'POST':
        # Recupera el cliente existente por su ID
        cliente = Clientes.query.get(id_cliente)
        # Actualiza los campos del cliente con los datos del formulario
        cliente.id_cliente = request.form['id_cliente']
        cliente.tipo_doc = request.form['tipo_doc']
        cliente.nombre = request.form['nombre']
        cliente.apellido = request.form['apellido']
        cliente.tipo_persona = request.form['tipo_persona']
        cliente.telefono = request.form['telefono']
        cliente.direccion = request.form['direccion']
        cliente.ciudad = request.form['ciudad']
        cliente.correo = request.form['correo']

        # Confirma los cambios en la base de datos
        db.session.commit()
        # Redirige a la página de lista de clientes después de actualizar
        return redirect(url_for('cliente.clientes'))
    
    # Si la solicitud es GET, muestra el formulario de actualización
    cliente = Clientes.query.get(id_cliente)
    return render_template('/actualizarcliente.html', cliente=cliente)

# Ruta para eliminar un cliente específico
@cliente.route("/eliminarcliente/<id_cliente>")
def eliminar_cliente(id_cliente):
    # Recupera el cliente por su ID
    cliente = Clientes.query.get(id_cliente)
    # Elimina el cliente de la base de datos
    db.session.delete(cliente)
    # Confirma los cambios en la base de datos
    db.session.commit()
    # Redirige a la página de lista de clientes después de eliminar
    return redirect(url_for('cliente.clientes'))