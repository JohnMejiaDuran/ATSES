from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.atses import Estructuras
from utils.db import db

#creacion del Blueprint para estructuras
estructura = Blueprint("estructura", __name__)

#Ruta para mostrar la lista de estructuras
@estructura.route("/estructuras")
def estructuras():
    #Recupera todas las estructuras de la bae de datos
    estructuras = Estructuras.query.all()
    #Renderiza la plantilla "estructuras.html" y pasa la lista de clientes como contexto
    return render_template("estructuras.html",estructuras=estructuras)

#Ruta para procesar el formulario de resgitro de Estructuras

@estructura.route("/registroestructura", methods=['POST'])
def registro_estructrua():
    id_material = request.form['id_material']
    id_fabricacion = request.form['id_fabricacion']
    diseño = request.form['diseño']
    nombre = request.form ['nombre']
    precio_venta = request.form['precio_venta']
    valor_5deaccesorios=request.form['valor_5deaccesorios']
    descripciondeaccesorios=request.form['descripciondeaccesorios']
    valor_6manodeobra = request.form['valor_6manodeobra']
    altura= request.form['altura']
    ancho = request.form['ancho']
    margen_perdidamaterial = request.form['margen_perdidamaterial']
    costoenmaterial = request.form['costoenmaterial']
    valor_insumos = request.form['valor_insumos']
    
    #Crea un nuevo objeto Estructuras con los datos del formulario
    
    nueva_estructura = Estructuras(id_fabricacion,id_material,diseño,nombre,precio_venta,valor_5deaccesorios,descripciondeaccesorios,valor_6manodeobra,altura,ancho,margen_perdidamaterial,costoenmaterial,valor_insumos)
    
    #Agrega la nueva estructura a la sesion de base de datos
    db.session.add(nueva_estructura)
    
    #Confirma los cambios en la base de datos
    db.session.commit()
    
    categoria = obtener_categoria_mensaje("guardado")
    flash("Estructura guardada satisfactoriamente",categoria)
    
    #Redirige a la pagina de lista de estructuras despues de registrar una nueva 
    
    return redirect(url_for ('estructura.estructuras'))

# Ruta para actualizar una estructura en especifico

@estructura.route("/actulizarestructura/<id_fabricacion>", methods=['POST','GET'])
def actualizar_estructura (id_fabricacion):
    if request.method=='POST':
        # Recupera la estructura exitente por su id
        estructura = Estructuras.query.get(id_fabricacion)
        
        # Actualiza los campos de la estructura con los datos del formulario
        
        estructura.id_material = request.form['id_material']
        estructura.id_fabricacion=request.form['id_fabricacion']
        estructura.diseño=request.form ['diseño']
        estructura.nombre=request.form ['nombre']
        estructura.precio_venta=request.form['precio_venta']
        estructura.valor_5deaccesorios=request.form ['valor_5deaccesorios']
        estructura.descripciondeaccesorios=request.form ['descripciondeaccesorios']
        estructura.valor_6manodeobra=request.form ['valor_6manodeobra']
        estructura.altura= request.form['altura']
        estructura.ancho = request.form['ancho']
        estructura.margen_perdidamaterial = request.form['margen_perdidamaterial']
        estructura.costoenmaterial = request.form['costoenmaterial']
        estructura.valor_insumos = request.form['valor_insumos']
        
        db.session.commit()
        
        categoria = obtener_categoria_mensaje("estructura actualizada satisfactoriamente")
        flash("estructura actualizada satisfactoriamente", categoria) 
        # Redirige a la página de lista de estructuras después de actualizar
        return redirect(url_for('estructura.estructuras'))
    
        # Si la solicitud es GET, muestra el formulario de actualización
    estructura = Estructuras.query.get(id_fabricacion)
    return render_template('/actualizarestructura.html', estructura=estructura)

# Ruta para eliminar un cliente específico
@estructura.route("/eliminarestructura/<id_fabricacion>")
def eliminar_estructura(id_fabricacion):
    # Recupera la estructura por su ID
    estructura = Estructuras.query.get(id_fabricacion)
    # Elimina a la estructura de la base de datos
    db.session.delete(estructura)
    # Confirma los cambios en la base de datos
    db.session.commit()
    # Redirige a la página de lista de estructuras después de eliminar
    categoria = obtener_categoria_mensaje("Estructura eliminada satisfactoriamente")
    flash("Estructura eliminada satisfactoriamente", categoria)

    return redirect(url_for('estructura.estructuras'))


def obtener_categoria_mensaje(mensaje):
    # Determina la categoría basada en el contenido del mensaje
    if "guardada" in mensaje:
        return "success"
    elif "actualizada" in mensaje:
        return "warning"
    elif "eliminada" in mensaje:
        return "danger"
    else:
        return "info"