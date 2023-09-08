from flask import Flask
from routes.atses import atses

app = Flask(__name__)

app.register_blueprint(atses)