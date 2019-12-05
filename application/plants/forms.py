from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, validators

errorA = "Nimen tulee olla 3-30 merkkiä pitkä"

class PlantForm(FlaskForm):
    name = StringField(" Kasvin nimi", [validators.Length(min=3, max=30, message=errorA)])
    pest = BooleanField("Tuholaisia")
  
    class Meta:
        csrf = False

  