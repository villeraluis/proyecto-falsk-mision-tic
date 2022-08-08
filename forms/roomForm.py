from wtforms import StringField, validators, SubmitField,IntegerField
from flask_wtf import FlaskForm

class RoomForm(FlaskForm):
    number= IntegerField('Numero de Habitación',[validators.DataRequired()])
    description= StringField('Descripción',[validators.Length(max=250)])
    submit = SubmitField(label=('Crear Habitacion'))