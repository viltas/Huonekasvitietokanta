from application import app, db
from flask import redirect, render_template, request, url_for
from application.species.models import Species
from application.species.forms import SpeciesForm
from flask_login import login_required, current_user

@app.route("/species", methods=["GET"])
@login_required
def species_index():
    return render_template("species/list.html", species = Species.query.all())

@app.route("/species/new/")
@login_required
def species_form():
    return render_template("species/new.html", form = SpeciesForm())

@app.route("/species/", methods=["POST"])
@login_required
def species_create():
    form = SpeciesForm(request.form)

    if not form.validate():
        return render_template("species/new.html", form = form)

    t = Species(form.genus.data, form.epithet.data, form.name.data, form.water.data, form.light.data)
 

    db.session().add(t)
    db.session().commit()

    return redirect(url_for("species_index"))

@app.route("/species/<species_id>/delete", methods=["POST"])
def species_delete(species_id):
    t = Species.query.get(species_id)
    db.session().delete(t)
    db.session().commit()

    print("Lajikuvaus poistettu")

    return redirect(url_for("species_index"))

    
