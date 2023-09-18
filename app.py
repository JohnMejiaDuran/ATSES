from flask import Flask
from routes.clientes import cliente
from routes.home import home
from routes.proveedores import proveedor
from routes.usuarios import usuario
from routes.materiales import material
from routes.login import login
from utils.db import bcrypt
from routes.estructuras import estructura


app = Flask(__name__)


app.secret_key = "secret key"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:@localhost/atsesdb"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


bcrypt.init_app(app)


app.register_blueprint(cliente)
app.register_blueprint(home)
app.register_blueprint(proveedor)
app.register_blueprint(usuario)
app.register_blueprint(material)
app.register_blueprint(login)
app.register_blueprint(estructura)
