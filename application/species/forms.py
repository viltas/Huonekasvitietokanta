from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, IntegerField, SelectField, validators

errorA = "Suvun nimen tulee olla 3-30 merkkiä pitkä"
errorB = "Epiteetin tulee olla 3-30 merkkiä pitkä"
errorC = "Nimen tulee olla 3-30 merkkiä pitkä"

class SpeciesForm(FlaskForm):
    genus = StringField("Suku: ", [validators.Length(min=3, max=30, message=errorA)])
    epithet = StringField("Epiteetti: ", [validators.Length(min=3, max=30, message=errorB)])
    name = StringField("Nimi: ", [validators.Length(min=3, max=30, message=errorC)])
    water = SelectField(u'Vedentarve: ', choices=[('vähäinen', 'vähäinen'), ('kohtalainen', 'kohtalainen'), ('tasainen kosteus', 'tasainen kosteus')])
    light = SelectField(u'Valontarve: ', choices=[('varjo', 'varjo'), ('puolivarjo', 'puolivarjo'), ('hajavalo', 'hajavalo'), ('runsas valo', 'runsas valo')])
  
    class Meta:
        csrf = False

  