from application import app, db
from flask import redirect, render_template, request, url_for
from application.plants.models import Plant

@app.route("/plants", methods=["GET"])
def plants_index():
    return render_template("plants/list.html", plants = Plant.query.all())

@app.route("/plants/new/")
def plants_form():
    return render_template("plants/new.html")

@app.route("/plants/<plant_id>/", methods=["POST"])
def plants_set_pest(plant_id):

    t = Plant.query.get(plant_id)
    if t.pest == False:
      t.pest = True
    elif t.pest == True:
      t.pest = False
    db.session().commit()
  
    return redirect(url_for("plants_index"))

@app.route("/plants/", methods=["POST"])
def plants_create():
    t = Plant(request.form.get("name"))

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("plants_index"))