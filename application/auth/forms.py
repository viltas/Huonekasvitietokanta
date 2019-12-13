from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators, ValidationError
from application.auth.models import User



class LoginForm(FlaskForm):
    username = StringField("Käyttäjätunnus: ")
    password = PasswordField("Salasana: ")    
  
    class Meta:
        csrf = False

errorA = "Nimen tulee olla 3-30 merkkiä pitkä"
errorAA = "Käyttäjänimi on jo käytössä"
errorB = "Käyttäjätunnuksen tulee olla 3-10 merkkiä pitkä"
errorC = "Salasanan tulee olla 10-30 merkkiä pitkä"


class Unique(object):
    """ validator that checks field uniqueness """
    def __init__(self, model, field, message=None):
        self.model = model
        self.field = field
        if not message:
            message = u'Käyttäjätunnus on jo käytössä'
        self.message = message

    def __call__(self, form, field):         
        check = self.model.query.filter(self.field == field.data).first()
        if check:
            raise ValidationError(self.message)

class AuthForm(FlaskForm):
    name = StringField("Nimi: ", [validators.Length(min=3, max=30, message=errorA)])
    username = StringField("Käyttäjätunnus: ", [validators.Length(min=3, max=10, message=errorB), Unique(User, User.username)])
    password = PasswordField("Salasana: ", [validators.Length(min=6, max=30, message=errorC)])



    
    
  
    class Meta:
        csrf = False        
