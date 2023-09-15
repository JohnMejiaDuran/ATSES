from flask import Flask
from routes.clientes import cliente
from routes.home import home
from routes.proveedores import proveedor


app = Flask(__name__)
app.secret_key = "secret key"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://Marly:sofia120329@localhost/atsesdb"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.register_blueprint(cliente)
app.register_blueprint(home)
app.register_blueprint(proveedor)

