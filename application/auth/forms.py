from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators

class LoginForm(FlaskForm):
    username = StringField("Käyttäjätunnus: ")
    password = PasswordField("Salasana: ")    
  
    class Meta:
        csrf = False

errorA = "Nimen tulee olla 3-30 merkkiä pitkä"
errorB = "Käyttäjätunnuksen tulee olla 3-10 merkkiä pitkä"
errorC = "Salasanan tulee olla 10-30 merkkiä pitkä"


class AuthForm(FlaskForm):
    name = StringField("Nimi: ", [validators.Length(min=3, max=30, message=errorA)])
    username = StringField("Käyttäjätunnus: ", [validators.Length(min=3, max=10, message=errorB)])
    password = PasswordField("Salasana: ", [validators.Length(min=6, max=30, message=errorC)])
    
  
    class Meta:
        csrf = False        
