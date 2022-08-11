from utils.db import db
from models.comment import Comment
from models.room import Room

class Reservation(db.Model):
    __tablename__ = 'reservations'
    id = db.Column(db.Integer, primary_key=True)
    date_from = db.Column(db.DateTime(),nullable=False)
    date_to = db.Column(db.DateTime(),nullable=False)
    status= db.Column(db.String(50),nullable=False)
    room_id = db.Column(db.Integer, db.ForeignKey('rooms.id'),nullable=False)
    user_id = db.Column(db.String(20), db.ForeignKey('users.id_number'),nullable=False)
    comments = db.relationship('Comment', backref='reservation', lazy=True)
    

   