from flask_wtf import FlaskForm
from wtforms import widgets
from wtforms import BooleanField, StringField, SelectField, validators
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from application.species.models import Species


errorA = "Nimen tulee olla 3-30 merkkiä pitkä"




class PlantForm(FlaskForm):
    name = StringField(" Kasvin nimi", [validators.Length(min=3, max=30, message=errorA)])
    pest = BooleanField("Tuholaisia")
    species_id = QuerySelectField("Laji: ", query_factory=lambda: Species.query.all(), get_label='name')
   

  
    class Meta:
        csrf = False

  