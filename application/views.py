from flask import render_template
from application import app
from application.auth.models import User
from application.species.models import Species







@app.route('/')
def index():

    return render_template("index.html", current_species=Species.find_current_species(), greenthumbs=User.find_greenthumbs())    
