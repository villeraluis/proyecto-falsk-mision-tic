from wtforms import StringField, validators, SubmitField,IntegerField,BooleanField
from flask_wtf import FlaskForm

class RoomForm(FlaskForm):
    number= IntegerField('Numero de Habitación',[validators.DataRequired()])
    description= StringField('Descripción',[validators.Length(max=250)])
    is_enable= BooleanField('Habilitada', default=True)
    submit = SubmitField(label=('Crear Habitacion'))