from wtforms import  StringField, PasswordField, validators, SubmitField
from flask_wtf import FlaskForm

class Login(FlaskForm):
    user_name= StringField('Nombre De Usuario',[validators.Length(min=4, max=25),validators.DataRequired()])
    pasword= PasswordField('Contraseña',[validators.Length(min=4, max=25),validators.DataRequired()])
    submit = SubmitField(label=('Ingresar'))
