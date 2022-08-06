from utils.db import db

class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.int)
    description = db.Column(db.String(25))
    
    def __init__(self, number, description):
        self.number = number
        self.description = description
        
