from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, validators

class PlantForm(FlaskForm):
    name = StringField(" Tuholaisen nimi nimi", [validators.Length(min=2)])
    name = StringField(" Tuholaisen torjuntatapa", [validators.Length(min=2)])
    
  
    class Meta:
        csrf = False

  