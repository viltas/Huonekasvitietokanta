# flask-sovellus
from flask import Flask


app = Flask(__name__)


# tietokanta
from flask_sqlalchemy import SQLAlchemy
import os

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///plants.db"    
    app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)


# oma login_required

from functools import wraps
from application.auth import models
from flask_login import current_user 


def login_required(role = "ANY"):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            if not current_user:
                return login_manager.unauthorized()
            if not current_user.is_authenticated:
                return login_manager.unauthorized()
            unauthorized = False

            if not role == "ANY":
                unauthorized = True
                for user_role in current_user.userrole():
                    if user_role == role:
                        unauthorized = False
                        break
            if unauthorized:
                return login_manager.unauthorized()
            return fn(*args, **kwargs)
        return decorated_view
    return wrapper



# oman sovelluksen toiminnallisuudet
from application import views
from application import models

from application.plants import models
from application.plants import views

from application.species import models
from application.species import views

from application.pests import models
from application.pests import views

from application.auth import models
from application.auth import views

# kirjautuminen
from application.auth.models import User
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Kirjaudu sisään käyttääksesi tätä toimintoa."

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# luodaan taulut tietokantaan tarvittaessa
db.create_all()