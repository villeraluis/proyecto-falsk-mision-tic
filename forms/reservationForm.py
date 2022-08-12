from wtforms import Form, BooleanField, StringField, PasswordField, validators, SubmitField,IntegerField,DateTimeLocalField,DateField,SelectField
from flask_wtf import FlaskForm



class ReservationForm(FlaskForm):
    date_from=DateTimeLocalField('Fecha de Inicio',[validators.DataRequired()],format='%Y-%m-%dT%H:%M')
    date_to=DateTimeLocalField('Fecha Final', [validators.DataRequired()],format='%Y-%m-%dT%H:%M')
    room_id= SelectField('Habitación',choices=[] , coerce=int)
    user_id = SelectField('Usuario',choices=[] , coerce=int)
    submit = SubmitField(label=('Crear Reserva'))
    
    
class ReservationFormUser(FlaskForm):
    date_from=DateTimeLocalField('Fecha de Inicio',[validators.DataRequired()],format='%Y-%m-%dT%H:%M')
    date_to=DateTimeLocalField('Fecha Final', [validators.DataRequired()],format='%Y-%m-%dT%H:%M')
    room_id= SelectField('Habitación',choices=[] , coerce=int)
    submit = SubmitField(label=('Crear Reserva'))