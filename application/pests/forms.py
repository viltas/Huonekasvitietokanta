from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, validators, ValidationError, TextAreaField
from application.pests.models import Pest


errorA = "Nimen tulee olla 3-30 merkkiä pitkä"
errorB = "Torjunnan kuvauksen tulee olla 0-500 merkkiä pitkä"

class Unique(object):
    """ validator that checks field uniqueness """
    def __init__(self, model, field, message=None):
        self.model = model
        self.field = field
        if not message:
            message = u'Tämä nimi on jo käytössä'
        self.message = message

    def __call__(self, form, field):         
        check = self.model.query.filter(self.field == field.data).first()
        if check:
            raise ValidationError(self.message)

class PestForm(FlaskForm):
    name = StringField(" Tuholaisen nimi", [validators.Length(min=3, max=30, message=errorA), Unique(Pest, Pest.name)])
    control = TextAreaField(" Tuholaisen torjuntatapa", [validators.Length(min=0, max=500, message=errorB)])
    
  
    class Meta:
        csrf = False

  