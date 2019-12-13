from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, IntegerField, SelectField, validators, ValidationError
from application.species.models import Species

errorA = "Suvun nimen tulee olla 3-30 merkkiä pitkä"
errorB = "Epiteetin tulee olla 3-30 merkkiä pitkä"
errorC = "Nimen tulee olla 3-30 merkkiä pitkä"

class Unique(object):
    """ validator that checks field uniqueness """
    def __init__(self, model, field, message=None):
        self.model = model
        self.field = field
        if not message:
            message = u'Lajinimi on jo käytössä'
        self.message = message

    def __call__(self, form, field):         
        check = self.model.query.filter(self.field == field.data).first()
        if check:
            raise ValidationError(self.message)

class SpeciesForm(FlaskForm):
    genus = StringField("Suku: ", [validators.Length(min=3, max=30, message=errorA)])
    epithet = StringField("Epiteetti: ", [validators.Length(min=3, max=30, message=errorB)])
    name = StringField("Nimi: ", [validators.Length(min=3, max=30, message=errorC), Unique(Species, Species.name)])
    water = SelectField(u'Vedentarve: ', choices=[('vähäinen', 'vähäinen'), ('kohtalainen', 'kohtalainen'), ('tasainen kosteus', 'tasainen kosteus')])
    light = SelectField(u'Valontarve: ', choices=[('varjo', 'varjo'), ('puolivarjo', 'puolivarjo'), ('hajavalo', 'hajavalo'), ('runsas valo', 'runsas valo')])
  
    class Meta:
        csrf = False

  