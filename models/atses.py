from utils.db import db


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

