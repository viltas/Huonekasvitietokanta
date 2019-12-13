from application import app, db
from flask import redirect, render_template, request, url_for
from application.pests.models import Pest
from application.plants.models import Plant, PlantPest
from application.plants.forms import PlantForm, PlantEditForm, PlantPestForm
from flask_login import login_required, current_user
from application.species.models import Species


@app.route("/plants", methods=["GET"])
@login_required
def plants_index():
    return render_template("plants/list.html", plants = Plant.query.filter_by(account_id=current_user.id))




@app.route("/plants/list_infections", methods=["GET"])
@login_required
def plantpest_index():
    return render_template("plants/list_infections.html", infections = PlantPest.query.filter_by(account_id=current_user.id))    




@app.route("/plants/new/")
@login_required
def plants_form():
    return render_template("plants/new.html", form = PlantForm())



@app.route("/plants/edit/<plant_id>/", methods=["GET", "POST"])
@login_required
def plants_edit(plant_id):

    p = Plant.query.get(plant_id)
    if request.method == "GET":
        form = PlantEditForm()
        form.name.data = p.name
        form.plant_id.data = p.plant_id
        
        return render_template( "plants/edit.html", form = form, plant = p)

    form = PlantEditForm(request.form)

    invalid = False
    if not form.validate():
        invalid = True    

    if invalid:
        return render_template(
            "plants/edit.html", form = form, auction = p)

    p.name = form.name.data
    p.species_id = form.species_id.data

    db.session().commit()

    return redirect(url_for("plants_index")) 




@app.route("/plants/new_infection/")
@login_required
def plantpest_form():
    return render_template("plants/new_infection.html", form = PlantPestForm())    




@app.route("/plants/", methods=["POST"])
@login_required
def plants_create():
    form = PlantForm(request.form)
    if not form.validate():
        return render_template("plants/new.html", form = form)

    speciesId = request.form.get('species_id', type=int)

    sp = Species.query.get(speciesId)

    p = Plant(form.name.data)
    p.species_id = speciesId
    p.account_id = current_user.id
    p.species_name = sp.name

    db.session().add(p)   
    db.session().commit()


    return redirect(url_for("plants_index"))





@app.route("/plants/new_infection/", methods=["POST"])
@login_required
def infection_create():
    form = PlantPestForm(request.form)
    if not form.validate():
        return render_template("plants/new_infection.html", form = form)

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

@app.route("/plants/<plant_id>/delete", methods=["POST"])
def plants_delete(plant_id):
    t = Plant.query.get(plant_id)
    db.session().delete(t)
    db.session().commit()

    print("Kasvi poistettu")

    return redirect(url_for("plants_index"))


@app.route("/plants/<infection_id>/delete_infection", methods=["POST"])
def infection_delete(infection_id):
    i = PlantPest.query.get(infection_id)
    db.session().delete(i)
    db.session().commit()

    print("Tartunta poistettu")

    return redirect(url_for("plantpest_index"))    