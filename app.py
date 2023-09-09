from flask import Flask
from routes.clientes import atses

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:@localhost/atsesdb"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.register_blueprint(atses)
