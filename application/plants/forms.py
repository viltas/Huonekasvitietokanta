from flask_wtf import FlaskForm
from wtforms import widgets
from wtforms import BooleanField, StringField, SelectField, FieldList, FormField, validators, ValidationError
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from application.species.models import Species
from application.plants.models import Plant, PlantPest
from application.pests.models import Pest
from flask_login import login_required, current_user


errorA = "Nimen tulee olla 3-30 merkkiä pitkä"

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

class PlantPestForm(FlaskForm):

    plant_id = QuerySelectField("Kasvi: ", query_factory=lambda: Plant.query.filter_by(account_id=current_user.id), get_label='name')
    pest_id = QuerySelectField("Tuholainen: ", query_factory=lambda: Pest.query.all(), get_label='name')

    class Meta:
        csrf = False

class PlantForm(FlaskForm):
    name = StringField(" Kasvin nimi", [validators.Length(min=3, max=30, message=errorA), Unique(Plant, Plant.name)])
    species_id = QuerySelectField("Laji: ", query_factory=lambda: Species.query.all(), get_label='name')
  
    class Meta:
        csrf = False

class PlantEditForm(FlaskForm):
    name = StringField(" Kasvin nimi", [validators.Length(min=3, max=30, message=errorA)])
    species_id = QuerySelectField("Laji: ", query_factory=lambda: Species.query.all(), get_label='name')
  
    class Meta:
        csrf = False        

