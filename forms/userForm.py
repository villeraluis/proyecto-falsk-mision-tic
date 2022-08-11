from wtforms import Form, BooleanField, StringField, PasswordField, validators, SubmitField,IntegerField,EmailField,DateField
from flask_wtf import FlaskForm

class UserForm(FlaskForm):
    id_number= IntegerField('Numero de Cedula',[validators.DataRequired()])
    name= StringField('Nombres',[validators.Length(min=4, max=25),validators.DataRequired()])
    last_name= StringField('Apellidos',[validators.Length(min=4, max=25),validators.DataRequired()])
    email= EmailField('Correo',[validators.Length(min=4, max=25),validators.DataRequired(),validators.Email()])
    date_birth= DateField('Fecha de Nacimiento',[validators.DataRequired()])
    user_name= StringField('Nombre De Usuario',[validators.Length(min=4, max=25),validators.DataRequired()])
    pasword= PasswordField('Contraseña',[validators.Length(min=4, max=25),validators.DataRequired(), validators.EqualTo('confirm')])
    confirm = PasswordField('Confirmar Contraseña',[validators.DataRequired()])
    submit = SubmitField(label=('Crear Cuenta'))
    
       
class ClientForm(FlaskForm):
    address= StringField('Dirección',[validators.Length(min=7, max=50),validators.DataRequired()])
    phone= StringField('Telefono',[validators.Length(min=7, max=20),validators.DataRequired()])
    

    
    