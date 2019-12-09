from flask import render_template
from application import app
from application.auth.models import User



@app.route('/')
def index():
    return render_template("index.html", max_plants=User.find_user_with_max_plants())    
