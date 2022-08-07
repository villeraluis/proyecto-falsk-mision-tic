from utils.db import db

class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(50),nullable=False)
    rating = db.Column(db.Integer,nullable=False)
    reservation_id = db.Column(db.Integer, db.ForeignKey('reservations.id'),nullable=False)
    
    
    def __init__(self, description):
        self.description = description
       