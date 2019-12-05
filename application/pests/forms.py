from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, validators


errorA = "Nimen tulee olla 3-30 merkkiä pitkä"
errorA = "Torjunnan kuvauksen tulee olla 5-50 merkkiä pitkä"

class PlantForm(FlaskForm):
    name = StringField(" Tuholaisen nimi nimi", [validators.Length(min=3, max=30, message=errorA)])
    name = StringField(" Tuholaisen torjuntatapa", [validators.Length(min=5, max=50, message=errorB)])
    
  
    class Meta:
        csrf = False

  