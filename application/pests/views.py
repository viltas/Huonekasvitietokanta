from application import app, db, login_required
from flask import redirect, render_template, request, url_for
from application.pests.models import Pest
from application.plants.models import Plant, PlantPest
from application.pests.forms import PestForm



# app route for listing the pests in the database

@app.route("/pests", methods=["GET"])
@login_required(role="ANY")
def pests_index():
    return render_template("pests/list.html", pests = Pest.query.all())


# app route for the new pest form

@app.route("/pests/new/")
@login_required(role="ADMIN")
def pests_form():
    return render_template("pests/new.html", form = PestForm())


# app route for saving a new pest to the database

@app.route("/pests/<pest_id>/", methods=["POST"])
@login_required(role="ADMIN")
def pests_set_pest(pest_id):

    t = Pest.query.get(pest_id)
    if t.pest == False:
      t.pest = True
    elif t.pest == True:
      t.pest = False
    db.session().commit()
  
    return redirect(url_for("pests_index"))


# app route for saving a new pest to the database

@app.route("/pests/", methods=["POST"])
@login_required(role="ADMIN")
def pests_create():
    form = PestForm(request.form)

    if not form.validate():
        return render_template("pests/new.html", form = form)

    t = Pest(form.name.data, form.description.data, form.control.data)
 
    db.session().add(t)
    db.session().commit()

    return redirect(url_for("pests_index"))

# app route for deleting a pest

@app.route("/pests/<pest_id>/delete", methods=["POST"])
@login_required(role="ADMIN")
def pests_delete(pest_id):
    t = Pest.query.get(pest_id)
    db.session().delete(t)
    db.session().commit()

    print("Tuholainen poistettu")

    return redirect(url_for("pests_index"))


# app route for editing the pest info

@app.route("/pests/edit/<pest_id>", methods=["POST"])
@login_required(role="ADMIN")
def pests_edit(pest_id):
    form = PestForm(request.form)
    pest = Pest.query.get(pest_id)
    form.name.data = pest.name
    form.description.data = pest.description
    form.control.data = pest.control

    return render_template("pests/edit.html", id=pest_id, form=form)


# app route for updating the pest info

@app.route("/pests/update/<pest_id>", methods=["POST"])
@login_required(role="ADMIN")
def pests_update(pest_id):

    form = PestForm(request.form)
    Pest.query.filter_by(id=pest_id).update(dict(name=form.name.data, description=form.description.data, control=form.control.data))
    PlantPest.query.filter_by(id=pest_id).update(dict(pest_name=form.name.data))


    db.session().commit()
    return redirect(url_for("pests_index"))


    
