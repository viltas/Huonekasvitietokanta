from flask import render_template
from application import app
from application.auth.models import User
from flask_login import current_user




@app.route('/')
def index():
    
    return render_template("index.html")    
