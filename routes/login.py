from flask import Blueprint, render_template, redirect, url_for
from utils.db import db,bcrypt
from models.atses import LoginForm, RegisterForm, User
from flask_login import login_user



login = Blueprint("login", __name__)


@login.route('/login', methods=['GET','POST'])
def log_in():
    form = LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('login.registro'))

    return render_template("login.html", form=form)

@login.route('/registrousuario', methods=['GET','POST'])

def registro():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        nuevo_usuario = User(username=form.username.data, password=hashed_password)
        db.session.add(nuevo_usuario)
        db.session.commit()
        return redirect(url_for('login.log_in'))

    return render_template("registrousuario.html", form=form)