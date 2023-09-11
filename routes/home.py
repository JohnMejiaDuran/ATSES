from flask import Blueprint, render_template, request, redirect, url_for
from models.atses import Clientes
from utils.db import db

home = Blueprint("home", __name__)


@home.route("/")
def index():
    return render_template("index.html")
