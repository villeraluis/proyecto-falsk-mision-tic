from utils.db import db
from datetime import date 



class Room(db.Model):
    __tablename__ = 'rooms'
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer,nullable=False)
    description = db.Column(db.String(25),nullable=True)
    is_enable= db.Column(db.Boolean,nullable=False,default=True)
    reservations = db.relationship('Reservation', backref='room', lazy=True)
    
    def last_reservation(self):  
        today= date.today() 
        for reservation in self.reservations:   
             return reservation 
             break
             
