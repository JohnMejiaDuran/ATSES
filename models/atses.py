from utils.db import db
from flask_login import UserMixin
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
class Clientes(db.Model):

    id_cliente = db.Column(db.Integer, primary_key=True)
    tipo_doc = db.Column(db.String(10))
    nombre = db.Column(db.String(150))
    apellido = db.Column(db.String(150))
    telefono = db.Column(db.String(20))
    direccion = db.Column(db.String(100))
    ciudad = db.Column(db.String(50))
    correo = db.Column(db.String(50))

    def __init__(self,id_cliente,tipo_doc,nombre,apellido,telefono,direccion,ciudad,correo):
        self.id_cliente = id_cliente
        self.tipo_doc = tipo_doc
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.direccion = direccion
        self.ciudad = ciudad
        self.correo = correo


class Proveedores(db.Model):
    id_proveedor = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(150))
    telefono = db.Column(db.String(20))
    direccion = db.Column(db.String(100))
    ciudad = db.Column(db.String(50))
    correo = db.Column(db.String(50))

    def __init__(self,id_proveedor, nombre, telefono, direccion, ciudad, correo):
        self.id_proveedor = id_proveedor
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        self.ciudad = ciudad
        self.correo = correo
        
        
class Usuarios(db.Model):
    id_vendedor = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(150))
    email = db.Column(db.String(50))
    contacto = db.Column(db.String(20))
    usuario = db.Column(db.String(100))
    contrasena = db.Column(db.String(50))
    

    def __init__(self,id_vendedor,nombre,email,contacto,usuario,contrasena):
        self.id_vendedor = id_vendedor
        self.nombre = nombre
        self.email = email     
        self.contacto = contacto
        self.usuario = usuario
        self.contrasena = contrasena
       


class Materiales(db.Model):
    id_material = db.Column(db.Integer, primary_key=True)
    id_proveedor = db.Column(db.String(150))
    nombre = db.Column(db.String(150))
    tipo = db.Column(db.String(150))
    forma = db.Column(db.String(150))
    calibre = db.Column(db.String(20))
    pulgada = db.Column(db.String(20))
    medida = db.Column(db.String(20))
    valor = db.Column(db.String(1000))
    

    def __init__(self,id_material,id_proveedor, nombre, tipo, forma, calibre, pulgada, medida,valor):
        self.id_material = id_material
        self.id_proveedor = id_proveedor
        self.nombre = nombre
        self.tipo = tipo
        self.forma = forma
        self.calibre = calibre
        self.pulgada = pulgada
        self.medida =medida
        self.valor =valor

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(20), nullable=False)


class RegisterForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(
        min=4, max=20)], render_kw={"placeholder": "Usario"})
    

    password = PasswordField(validators=[InputRequired(), Length(
        min=4, max=20)], render_kw={"placeholder": "Contraseña"})
    submit = SubmitField("Registro")    

    def validar_usuario(self, username):
        existe_usuario = User.query.filter_by(
            username=username.data).first()
        
        if existe_usuario:
            raise ValidationError(
                "Ya existe este usuario. Por favor selecciona otro."
            )

class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(
        min=4, max=20)], render_kw={"placeholder": "Username"})
    

    password = PasswordField(validators=[InputRequired(), Length(
        min=4, max=20)], render_kw={"placeholder": "Password"})
    submit = SubmitField("Login")    
        
class Estructuras(db.Model):
    id_material = db.Column(db.String(150))
    id_fabricacion = db.Column(db.Integer, primary_key=True)
    diseño = db.Column(db.String(150))
    nombre = db.Column(db.String(150))
    precio_venta = db.Column(db.String(150))
    valor_5deaccesorios = db.Column(db.String(150))
    descripciondeaccesorios = db.Column(db.String(20))
    valor_6manodeobra = db.Column(db.String(150))
    altura = db.Column(db.String(150))
    ancho = db.Column(db.String(150))
    margen_perdidamaterial = db.Column(db.String(150))
    costoenmaterial = db.Column(db.String(150))
    valor_insumos = db.Column(db.String(150))
    

    def __init__(self,id_fabricacion,id_material,diseño, nombre, precio_venta , valor_5deaccesorios,descripcciondeaccserios,valro_6demanodeobra,altura,ancho,margen_perdidamaterial,costoenmaterial,valor_insumos):
        self.id_material = id_material
        self.id_fabricacion = id_fabricacion
        self.diseño = diseño 
        self.nombre = nombre
        self.precio_venta = precio_venta 
        self.valor_5deaccesorios = valor_5deaccesorios
        self.descripciondeaccesorios=descripcciondeaccserios
        self.valor_6manodeobra = valro_6demanodeobra
        self.altura = altura
        self.ancho = ancho
        self.margen_perdidamaterial = margen_perdidamaterial
        self.costoenmaterial = costoenmaterial
        self.valor_insumos = valor_insumos
       
