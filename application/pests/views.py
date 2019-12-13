from application import app, db
from flask import redirect, render_template, request, url_for
from application.pests.models import Pest
from application.pests.forms import PestForm
from flask_login import login_required, current_user

@app.route("/pests", methods=["GET"])
@login_required
def pests_index():
    return render_template("pests/list.html", pests = Pest.query.all())

@app.route("/pests/new/")
@login_required
def pests_form():
    return render_template("pests/new.html", form = PestForm())

@app.route("/pests/<pest_id>/", methods=["POST"])
@login_required
def pests_set_pest(pest_id):

    t = Pest.query.get(pest_id)
    if t.pest == False:
      t.pest = True
    elif t.pest == True:
      t.pest = False
    db.session().commit()
  
    return redirect(url_for("pests_index"))

@app.route("/pests/", methods=["POST"])
@login_required
def pests_create():
    form = PestForm(request.form)

    if not form.validate():
        return render_template("pests/new.html", form = form)

    t = Pest(form.name.data, form.control.data)
 

    db.session().add(t)
    db.session().commit()

    return redirect(url_for("pests_index"))


@app.route("/pests/<pest_id>/delete", methods=["POST"])
def pests_delete(pest_id):
    t = Pest.query.get(pest_id)
    db.session().delete(t)
    db.session().commit()

    print("Tuholainen poistettu")

    return redirect(url_for("pests_index"))


    
