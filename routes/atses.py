from flask import Blueprint, render_template

atses = Blueprint("atses", __name__)


@atses.route("/")
def home():
    return render_template('index.html')

@atses.route('/clientes')
def clientes():
    return "<h1>clientes</h1>"