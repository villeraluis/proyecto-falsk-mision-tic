from utils.db import db


class Room(db.Model):
    __tablename__ = 'rooms'
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer,nullable=False)
    description = db.Column(db.String(25),nullable=True)
    reservations = db.relationship('Reservation', backref='room', lazy=True)
    
    def __init__(self, number, description):
        self.number = number
        self.description = description
        
