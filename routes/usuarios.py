from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.atses import Usuarios
from utils.db import db

# Creación del Blueprint para usuarios
usuario = Blueprint("usuario", __name__)

# Ruta para mostrar la lista de usuarios
@usuario.route("/usuarios")
def usuarios():
    # Recupera todos los usuarios de la base de datos
    usuario = Usuarios.query.all()
    # Renderiza la plantilla "usuarios.html" y pasa la lista de usuarios como contexto
    return render_template("usuarios.html", usuarios=usuario)

# Ruta para procesar el formulario de registro de usuarios
@usuario.route("/registrovendedor", methods=['POST'])
def registro_vendedor():
    # Recupera los datos del formulario
    id_vendedor = request.form['id_vendedor']
    nombre = request.form['nombre']
    email = request.form['email']
    contacto = request.form['contacto']
    usuario = request.form['usuario']
    contrasena = request.form['contrasena']
    
     # Recupera el cliente existente por su ID
    usuario = Usuarios.query.get(id_vendedor)
        
        # Actualiza los campos del cliente con los datos del formulario
    
    # Crea un nuevo objeto usuario con los datos del formulario
    nuevo_usuario = Usuarios(id_vendedor,  nombre, email, contacto, usuario, contrasena)
    
    # Agrega el nuevo usuario a la sesión de la base de datos
    db.session.add(nuevo_usuario)
    # Confirma los cambios en la base de datos
    db.session.commit()

    categoria = obtener_categoria_mensaje("guardado")
    flash("Usuario guardado satisfactoriamente", categoria)    

    # Redirige a la página de lista de clientes después de registrar uno nuevo
    return redirect(url_for('usuario.usuarios'))

# Ruta para actualizar un usuarios específico
@usuario.route("/actualizarvendedor/<id_vendedor>", methods=['POST','GET'])
def actualizar_vendedor(id_vendedor):
    if request.method == 'POST':
         # Recupera el cliente existente por su ID
        usuario = Usuarios.query.get(id_vendedor)
        # Actualiza los campos del cliente con los datos del formulario
        usuario.id_vendedor = request.form['id_vendedor']
        usuario.nombre = request.form['nombre']
        usuario.email = request.form['email']
        usuario.contacto = request.form['contacto']
        usuario.usuario = request.form['usuario']
        usuario.contrasena = request.form['contrasena']
       
       # Confirma los cambios en la base de datos
        db.session.commit()

        categoria = obtener_categoria_mensaje("Usuario actualizado satisfactoriamente")
        flash("Usuario actualizado satisfactoriamente", categoria) 
        # Redirige a la página de lista de usuarios después de actualizar
        return redirect(url_for('usuario.usuarios'))
    
    # Si la solicitud es GET, muestra el formulario de actualización
    usuario = Usuarios.query.get(id_vendedor)
    return render_template('/actualizarvendedor.html', usuario=usuario)

# Ruta para eliminar un cusuario específico
@usuario.route("/eliminarusuario/<id_vendedor>")
def eliminar_usuario(id_vendedor):
    # Recupera el cliente por su ID
    usuario = Usuarios.query.get(id_vendedor)
    # Elimina el cliente de la base de datos
    db.session.delete(usuario)
    # Confirma los cambios en la base de datos
    db.session.commit()
    # Redirige a la página de lista de usuarios después de eliminar
    categoria = obtener_categoria_mensaje("Usuario eliminado satisfactoriamente")
    flash("Usuario eliminado satisfactoriamente", categoria)

    return redirect(url_for('usuario.usuarios'))


def obtener_categoria_mensaje(mensaje):
    # Determina la categoría basada en el contenido del mensaje
    if "guardado" in mensaje:
        return "success"
    elif "actualizado" in mensaje:
        return "warning"
    elif "eliminado" in mensaje:
        return "danger"
    else:
        return "info"