from utils.db import db

class Clientes(db.Model):
    id_cliente = db.Column(db.Integer, primary_key = True)
    tipo_doc = db.Column(db.String(10))
    nombre = db.Column(db.String(150))
    apellido = db.Column(db.String(150))
    tipo_persona = db.Column(db.String(20))
    telefono = db.Column(db.String(20))
    direccion = db.Column(db.String(150))
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