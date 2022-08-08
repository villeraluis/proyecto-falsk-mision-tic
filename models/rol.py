from utils.db import db
from models.user import User



class Rol(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(50), unique=True,nullable=False)
    users = db.relationship('User', backref='role')

    
       