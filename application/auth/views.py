from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user
  
from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm
from application.auth.forms import AuthForm
from flask_login import login_required, current_user



@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)
    # mahdolliset validoinnit

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form,
                                error = "Väärä käyttäjätunnus tai salasana.")


    login_user(user)
    return redirect(url_for("index"))

@app.route("/auth", methods=["GET"])
@login_required
def auth_index():
    return render_template("auth/list.html", auth = User.query.all()) 

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/auth/new/")
def auth_new():
    if request.method == "GET":
        return render_template("auth/new.html", form = AuthForm())

@app.route("/auth/", methods=["POST"])
def auth_create():
    form = AuthForm(request.form)

    if not form.validate():
        return render_template("auth/new.html", form = form)

    t = User(form.name.data, form.username.data, form.password.data)

    db.session().add(t)
    db.session().commit()

    return redirect(url_for("auth_index"))

@app.route("/auth/<account_id>/delete", methods=["POST"])
def auth_delete(account_id):
    t = User.query.get(account_id)
    db.session().delete(t)
    db.session().commit()

    print("Käyttäjä poistettu")

    return redirect(url_for("auth_index"))    

