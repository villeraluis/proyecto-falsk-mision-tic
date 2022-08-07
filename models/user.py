
from werkzeug.security import (generate_password_hash, check_password_hash) 
from utils.db import db
from models.client import Client
from models.reservation import Reservation






class User(db.Model):
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
    
    
    def set_password(self, password): 
        self.password_hash = generate_password_hash(password) 
        
    def check_password(self, password): 
        return check_password_hash(self.password_hash, password)
   
    def __init__(self, id_number,name,last_name, email,date_birth,user_name,pasword,role_id):
        self.id_number = id_number
        self.name = name
        self.last_name = last_name
        self.email = email
        self.date_birth = date_birth
        self.user_name = user_name
        self.pasword= pasword
        self.role_id = role_id
        
article_list = db.relationship('ArticleList', back_populates='user')  
