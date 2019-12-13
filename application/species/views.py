from application import app, db, login_required
from flask import redirect, render_template, request, url_for
from application.species.models import Species
from application.plants.models import Plant
from application.auth.models import User
from application.species.forms import SpeciesForm
from flask_login import current_user 

@app.route("/species", methods=["GET"])
@login_required(role = "ANY")
def species_index():
    return render_template("species/list.html", species = Species.query.all())

@app.route("/species/new/")
@login_required(role = "ADMIN")
def species_form():
    return render_template("species/new.html", form = SpeciesForm())

@app.route("/species/", methods=["POST"])
@login_required(role="ADMIN")
def species_create():
    form = SpeciesForm(request.form)

    if not form.validate():
        return render_template("species/new.html", form = form)

    t = Species(form.genus.data, form.epithet.data, form.name.data, form.water.data, form.light.data)
 

    db.session().add(t)
    db.session().commit()

    return redirect(url_for("species_index"))

@app.route("/species/<species_id>/delete", methods=["POST"])
@login_required(role = "ADMIN")
def species_delete(species_id):
    t = Species.query.get(species_id)
    db.session().delete(t)
    db.session().commit()

    print("Lajikuvaus poistettu")

    return redirect(url_for("species_index"))


@app.route("/species/edit/<species_id>", methods=["POST"])
@login_required(role = "ADMIN")
def species_edit(species_id):

    form = SpeciesForm(request.form)
    species = Species.query.get(species_id)
    form.genus.data = species.genus
    form.epithet.data = species.epithet
    form.name.data = species.name
    form.water.data = species.water
    form.light.data = species.light
    
    
    return render_template("species/edit.html", id = species_id, form = form)

        


@app.route("/species/update/<species_id>", methods=["POST"])
@login_required(role = "ADMIN")
def species_update(species_id):

    form = SpeciesForm(request.form)
    Species.query.filter_by(id=species_id).update(
        dict(genus = form.genus.data, epithet = form.epithet.data, name = form.name.data, water = form.water.data, light = form.light.data))
    Plant.query.filter_by(id=species_id).update(dict(species_name=form.name.data))

    db.session().commit()
    return redirect(url_for("species_index"))

     

    
