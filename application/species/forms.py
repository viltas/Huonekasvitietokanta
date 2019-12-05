from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, IntegerField, validators

errorA = "Suvun nimen tulee olla 3-30 merkkiä pitkä"
errorB = "Epiteetin tulee olla 3-30 merkkiä pitkä"
errorC = "Nimen tulee olla 3-30 merkkiä pitkä"

class SpeciesForm(FlaskForm):
    genus = StringField("Suku: ", [validators.Length(min=3, max=30, message=errorA)])
    epithet = StringField("Epiteetti: ", [validators.Length(min=3, max=30, message=errorB)])
    name = StringField("Nimi: ", [validators.Length(min=3, max=30, message=errorC)])
    water = IntegerField('Vedentarve: ', [validators.NumberRange(min=1,max=5,message='Valitse väliltä 1-5')])
    light = IntegerField('Valontarve: ', [validators.NumberRange(min=1,max=5,message='Valitse väliltä 1-5')])
  
    class Meta:
        csrf = False

  