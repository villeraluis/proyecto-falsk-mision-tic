
from werkzeug.security import (check_password_hash) 
from flask_login import UserMixin
from utils.db import db
from models.client import Client
from models.reservation import Reservation

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id_number = db.Column(db.String(20), primary_key=True)
    name = db.Column(db.String(50),nullable=False)
    last_name = db.Column(db.String(50),nullable=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    date_birth = db.Column(db.Date())
    user_name = db.Column(db.String(64), unique=True, nullable=False)
    pasword = db.Column(db.String(128))
    confirm_email = db.Column(db.Date(),nullable=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'),nullable=False)
    client = db.relationship('Client', backref='user', lazy=True ,uselist=False)
    reservations = db.relationship('Reservation', backref='user', lazy=True)
    
         
    def check_password(self, password): 
        return check_password_hash(self.pasword, password)
   

    def get_id(self):
           return (self.id_number)  
       
    def is_admin(self):
	      return self.role_id==0 or self.role_id==1


