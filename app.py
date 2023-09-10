from flask import Flask
from routes.clientes import cliente
from routes.home import home
from routes.proveedores import proveedor

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:@localhost/atsesdb"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.register_blueprint(cliente)
app.register_blueprint(home)
app.register_blueprint(proveedor)