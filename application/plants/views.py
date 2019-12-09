from application import app, db
from flask import redirect, render_template, request, url_for
from application.plants.models import Plant
from application.plants.forms import PlantForm
from flask_login import login_required, current_user
from application.species.models import Species


@app.route("/plants", methods=["GET"])
@login_required
def plants_index():
    return render_template("plants/list.html", plants = Plant.query.filter_by(account_id=current_user.id))

@app.route("/plants/new/")
@login_required
def plants_form():
    return render_template("plants/new.html", form = PlantForm())

@app.route("/plants/<plant_id>/", methods=["POST"])
@login_required
def plants_set_pest(plant_id):

    t = Plant.query.get(plant_id)
    if t.pest == False:
      t.pest = True
    elif t.pest == True:
      t.pest = False
    db.session().commit()
  
    return redirect(url_for("plants_index"))


@app.route("/plants/", methods=["POST"])
@login_required
def plants_create():
    form = PlantForm(request.form)
    if not form.validate():
        return render_template("plants/new.html", form = form)

    speciesId = request.form.get('species_id', type=int)

    p = Plant(form.name.data)
    p.species_id = speciesId
    p.pest = form.pest.data
    p.account_id = current_user.id

    db.session().add(p)
    db.session().commit()


    return redirect(url_for("plants_index"))

@app.route("/plants/<plant_id>/delete", methods=["POST"])
def plants_delete(plant_id):
    t = Plant.query.get(plant_id)
    db.session().delete(t)
    db.session().commit()

    print("Kasvi poistettu")

    return redirect(url_for("plants_index"))
