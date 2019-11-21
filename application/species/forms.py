from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, IntegerField, validators

class SpeciesForm(FlaskForm):
    genus = StringField("Suku: ", [validators.Length(min=2)])
    epithet = StringField("Epiteetti: ", [validators.Length(min=2)])
    name = StringField("Nimi: ", [validators.Length(min=2)])
    water = IntegerField('Vedentarve: ', [validators.NumberRange(min=1,max=5,message='Valitse väliltä 1-5')])
    light = IntegerField('Valontarve: ', [validators.NumberRange(min=1,max=5,message='Valitse väliltä 1-5')])
  
    class Meta:
        csrf = False

  