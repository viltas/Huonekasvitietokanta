from application import app, db, login_required
from flask import redirect, render_template, request, url_for
from application.pests.models import Pest
from application.plants.models import Plant, PlantPest
from application.plants.forms import PlantForm, PlantPestForm
from flask_login import current_user
from application.species.models import Species


# app route for listing user's own plants

@app.route("/plants", methods=["GET"])
@login_required(role="ANY")
def plants_index():
    return render_template("plants/list.html", plants=Plant.query.filter_by(account_id=current_user.id))


# app route for listing the infections in user's plants

@app.route("/plants/list_infections", methods=["GET"])
@login_required(role="ANY")
def plantpest_index():
    return render_template("plants/list_infections.html", infections=PlantPest.query.filter_by(account_id=current_user.id))


# app route for the new plant form

@app.route("/plants/new/")
@login_required(role="ANY")
def plants_form():
    return render_template("plants/new.html", form=PlantForm())


# app route for the new infection form

@app.route("/plants/new_infection/")
@login_required(role="ANY")
def plantpest_form():
    return render_template("plants/new_infection.html", form=PlantPestForm())


# app route for saving a new plant to the database

@app.route("/plants/", methods=["POST"])
@login_required(role="ANY")
def plants_create():
    form = PlantForm(request.form)
    if not form.validate():
        return render_template("plants/new.html", form=form)

    speciesId = request.form.get('species_id', type=int)

    sp = Species.query.get(speciesId)

    p = Plant(form.name.data)
    p.species_id = speciesId
    p.account_id = current_user.id
    p.species_name = sp.name

    db.session().add(p)
    db.session().commit()

    return redirect(url_for("plants_index"))


# app route for saving a new infection to the database

@app.route("/plants/new_infection/", methods=["POST"])
@login_required(role="ANY")
def infection_create():
    form = PlantPestForm(request.form)
    if not form.validate():
        return render_template("plants/new_infection.html", form=form)

    plantId = request.form.get('plant_id', type=int)
    pestId = request.form.get('pest_id', type=int)

    pl = Plant.query.get(plantId)
    pe = Pest.query.get(pestId)

    i = PlantPest()
    i.plant_id = plantId
    i.pest_id = pestId
    i.plant_name = pl.name
    i.pest_name = pe.name
    i.account_id = current_user.id

    db.session().add(i)
    db.session().commit()

    return redirect(url_for("plantpest_index"))


# app route for deleting a plant from the database

@app.route("/plants/<plant_id>/delete", methods=["POST"])
@login_required(role="ANY")
def plants_delete(plant_id):

    plantId = plant_id
    PlantPest.query.filter_by(plant_id=plantId).delete()
    db.session().commit()

    t = Plant.query.get(plant_id)
    db.session().delete(t)
    db.session().commit()

    print("Kasvi poistettu")

    return redirect(url_for("plants_index"))


# app route for deleting an infection from a database

@app.route("/plants/<infection_id>/delete_infection", methods=["POST"])
@login_required(role="ANY")
def infection_delete(infection_id):
    i = PlantPest.query.get(infection_id)
    db.session().delete(i)
    db.session().commit()

    print("Tartunta poistettu")

    return redirect(url_for("plantpest_index"))


# app route for editing form of a plant already in a database
@app.route("/plants/edit/<plant_id>", methods=["POST"])
@login_required(role="ANY")
def plants_edit(plant_id):
    form = PlantForm(request.form)
    plant = Plant.query.get(plant_id)
    form.name.data = plant.name
    form.species_id.data = plant.species_id

    return render_template("plants/edit.html", id=plant_id, form=form)


# app route for updating the plant information

@app.route("/plants/update/<plant_id>", methods=["POST"])
@login_required(role="ANY")
def plants_update(plant_id):

    form = PlantForm(request.form)

    speciesId = request.form.get('species_id', type=int)
    sp = Species.query.get(speciesId)

    Plant.query.filter_by(id=plant_id).update(
        dict(name=form.name.data, species_id=speciesId, species_name=sp.name))

    db.session().commit()
    return redirect(url_for("plants_index"))
