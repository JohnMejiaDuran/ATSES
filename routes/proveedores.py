from flask import Blueprint, render_template, request, redirect, url_for
from models.atses import Proveedores
from utils.db import db

# Creación del Blueprint para Proveedores
proveedor = Blueprint("proveedor", __name__)


# Ruta para mostrar la lista de proveedores
@proveedor.route("/proveedores")
def proveedores():
    # Recupera todos los proveedores de la base de datos
    proveedores = Proveedores.query.all()
    # Renderiza la plantilla "proveedores.html" y pasa la lista de proveedores como contexto
    return render_template("proveedores.html", proveedores=proveedores)


# Ruta para mostrar el formulario de registro de proveedores
@proveedor.route("/registroproveedor")
def registrarproveedor():
    # Renderiza la plantilla "registroproveedor.html" para registrar nuevos proveedores
    return render_template("registroproveedor.html")


# Ruta para procesar el formulario de registro de proveedores
@proveedor.route("/registroproveedor", methods=["POST"])
def registro_proveedor():
    # Recupera los datos del formulario
    id_proveedor = request.form["id_proveedor"]
    nombre = request.form["nombre"]
    telefono = request.form["telefono"]
    direccion = request.form["direccion"]
    ciudad = request.form["ciudad"]
    correo = request.form["correo"]

    # Crea un nuevo objeto Proveedores con los datos del formulario
    nuevo_proveedor = Proveedores(
        id_proveedor, nombre, telefono, direccion, ciudad, correo
    )

    # Agrega el nuevo proveedor a la sesión de la base de datos
    db.session.add(nuevo_proveedor)
    # Confirma los cambios en la base de datos
    db.session.commit()

    # Redirige a la página de lista de proveedores después de registrar uno nuevo
    return redirect(url_for("proveedor.proveedores"))


# Ruta para actualizar un proveedor específico
@proveedor.route("/actualizarproveedor/<id_proveedor>", methods=["POST", "GET"])
def actualizar_proveedor(id_proveedor):
    if request.method == "POST":
        # Recupera el proveedor existente por su ID
        proveedor = Proveedores.query.get(id_proveedor)
        # Actualiza los campos del proveedor con los datos del formulario
        proveedor.id_proveedor = request.form["id_proveedor"]
        proveedor.nombre = request.form["nombre"]
        proveedor.telefono = request.form["telefono"]
        proveedor.direccion = request.form["direccion"]
        proveedor.ciudad = request.form["ciudad"]
        proveedor.correo = request.form["correo"]

        # Confirma los cambios en la base de datos
        db.session.commit()
        # Redirige a la página de lista de proveedores después de actualizar
        return redirect(url_for("proveedor.proveedores"))

    # Si la solicitud es GET, muestra el formulario de actualización
    proveedor = Proveedores.query.get(id_proveedor)
    return render_template("actualizarproveedor.html", proveedor=proveedor)


# Ruta para eliminar un proveedor específico
@proveedor.route("/eliminarproveedor/<id_proveedor>")
def eliminar_proveedor(id_proveedor):
    # Recupera el proveedor por su ID
    proveedor = Proveedores.query.get(id_proveedor)
    # Elimina el proveedor de la base de datos
    db.session.delete(proveedor)
    # Confirma los cambios en la base de datos
    db.session.commit()
    # Redirige a la página de lista de proveedores después de eliminar
    return redirect(url_for("proveedor.proveedores"))
