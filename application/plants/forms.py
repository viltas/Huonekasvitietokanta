from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, validators

class PlantForm(FlaskForm):
    name = StringField(" Kasvin nimi", [validators.Length(min=2)])
    pest = BooleanField("Tuholaisia")
  
    class Meta:
        csrf = False

  