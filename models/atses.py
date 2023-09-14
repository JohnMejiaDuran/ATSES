from utils.db import db


class Clientes(db.Model):
    id_cliente = db.Column(db.Integer, primary_key=True)
    tipo_doc = db.Column(db.String(10))
    nombre = db.Column(db.String(150))
    apellido = db.Column(db.String(150))
    tipo_persona = db.Column(db.String(20))
    telefono = db.Column(db.String(20))
    direccion = db.Column(db.String(100))
    ciudad = db.Column(db.String(50))
    correo = db.Column(db.String(50))

    def __init__(self,id_cliente,tipo_doc,nombre,apellido,tipo_persona,telefono,direccion,ciudad,correo):
        self.id_cliente = id_cliente
        self.tipo_doc = tipo_doc
        self.nombre = nombre
        self.apellido = apellido
        self.tipo_persona = tipo_persona
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
       