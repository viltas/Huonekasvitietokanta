from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user
from application import app, db, bcrypt, login_required
from application.auth.models import User
from application.plants.models import Plant, PlantPest
from application.auth.forms import LoginForm
from application.auth.forms import AuthForm
from flask_login import current_user


# app route for login with validators

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)


    user = User.query.filter_by(username=form.username.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form,
                                error = "Käyttäjätunnusta ei löytynyt!")
    
    checkPassword = bcrypt.check_password_hash(user.password, form.password.data)
    if not checkPassword:
        return render_template("auth/loginform.html", form = form,
                                error = "Väärä salasana!")
 
    login_user(user)
    return redirect(url_for("index"))


# app route for listing users (Admin only)

@app.route("/auth", methods=["GET"])
@login_required(role="ADMIN")
def auth_index():
    return render_template("auth/list.html", auth = User.query.filter(User.id != 1).all())

    

# app route for logout

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))


# app route for the new user form

@app.route("/auth/new/")
def auth_new():
    if request.method == "GET":
        return render_template("auth/new.html", form = AuthForm())


# app route for adding a new user to the database

@app.route("/auth/", methods=["POST"])
def auth_create():
    form = AuthForm(request.form)

    if not form.validate():
        return render_template("auth/new.html", form = form)

    hashPassword = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
    t = User(form.name.data, form.username.data, hashPassword)

    db.session().add(t)
    db.session().commit()

    return redirect(url_for("auth_index"))


# app route for deleting a user (Admin only)

@app.route("/auth/<account_id>/delete", methods=["POST"])
@login_required(role="ADMIN")
def auth_delete(account_id):

    accountId = account_id
    
    PlantPest.query.filter_by(account_id = accountId).delete()
    db.session().commit()
    Plant.query.filter_by(account_id = accountId).delete()
    db.session().commit()

    t = User.query.get(account_id)
    db.session().delete(t)
    db.session().commit()

    print("Käyttäjä poistettu")

    return redirect(url_for("auth_index"))    

