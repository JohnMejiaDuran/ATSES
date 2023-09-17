from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.atses import Materiales
from utils.db import db



# Creación del Blueprint para materiales
material = Blueprint("material", __name__)

# Ruta para mostrar la lista de materiales
@material.route("/materiales")
def materiales():
    # Recupera todos los materiales de la base de datos
    materiales =  Materiales.query.all()
    # Renderiza la plantilla "materiales.html" y pasa la lista de materiales como contexto
    return render_template("materiales.html", materiales=materiales)

# Ruta para mostrar el formulario de registro de material
@material.route("/registromaterial")
def registrarmaterial():
    # Renderiza la plantilla "registromaterial.html" para registrar nuevos materiales
    return render_template("registromaterial.html")

# Ruta para procesar el formulario de registro de materiales
@material.route("/registromaterial", methods=['POST'])
def registro_material():
    # Recupera los datos del formulario
    id_material = request.form['id_material']
    id_proveedor = request.form['id_proveedor']
    nombre = request.form['nombre']
    tipo = request.form['tipo']
    forma = request.form['forma']
    calibre = request.form['calibre']
    pulgada = request.form['pulgada']
    medida = request.form['medida']
    valor = request.form['valor']

   # Crea un nuevo objeto Materiales con los datos del formulario
    nuevo_material = Materiales(id_material, id_proveedor, nombre, tipo, forma, calibre, pulgada, medida, valor)
    
    # Agrega el nuevo material a la sesión de la base de datos
    db.session.add(nuevo_material)
    # Confirma los cambios en la base de datos
    db.session.commit()

    flash("Contacto guardado satisfactoriamente", 'success')    

    # Redirige a la página de lista de materiales después de registrar uno nuevo
    return redirect(url_for('material.materiales'))

# Ruta para actualizar un material específico
@material.route("/actualizarmaterial/<id_material>", methods=['POST','GET'])
def actualizar_material(id_material):
    if request.method == 'POST':
        # Recupera el material existente por su ID
        material = Materiales.query.get(id_material)
        # Actualiza los campos del material con los datos del formulario
        material.id_material = request.form['id_material']
        material.id_proveedor= request.form['id_proveedor']
        material.nombre = request.form['nombre']
        material.tipo = request.form['tipo']
        material.forma = request.form['forma']
        material.calibre = request.form['calibre']
        material.direccion = request.form['pulgada']
        material.medida = request.form['medida']
        material.valor = request.form['valor']

        # Confirma los cambios en la base de datos
        db.session.commit()
        # Redirige a la página de lista de materiales después de actualizar
        return redirect(url_for('material.materiales'))
    
    # Si la solicitud es GET, muestra el formulario de actualización
    material = Materiales.query.get(id_material)
    return render_template('/actualizarmaterial.html', material=material)

# Ruta para eliminar un cliente específico
@material.route("/eliminarmaterial/<id_material>")
def eliminar_material(id_material):
    # Recupera el cliente por su ID
    material = Materiales.query.get(id_material)
    # Elimina el cliente de la base de datos
    db.session.delete(material)
    # Confirma los cambios en la base de datos
    db.session.commit()
    # Redirige a la página de lista de clientes después de eliminar
    return redirect(url_for('material.materiales'))

