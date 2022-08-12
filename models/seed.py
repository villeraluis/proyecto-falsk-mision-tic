from ast import Try
from datetime import date
from models.rol import Rol
from .user import User
from utils.db import db
from werkzeug.security import (generate_password_hash) 
class seedRoles():
    def __init__(self):
        self.rol1=Rol(description="SuperAdministrador")
        self.rol2=Rol(description="Administrador")
        self.rol3=Rol(description="Cliente")
        
    def seed(self):
        try:
            db.session.add(self.rol1)
            db.session.add(self.rol2)
            db.session.add(self.rol3)
            db.session.commit()
        
        except:
           print("Nose registro los roles")
       


class seedAdmin():
    def __init__(self):
        self.user1=User(
            id_number="12345678",
            name="Admin",
            last_name="Admin",
            email='correo@admin.com',
            date_birth=date(2000,1,1),
            user_name='admin',
            pasword= generate_password_hash('admin'),
            is_enable=True,
            role_id=2)
        
    def seed(self):
        try:
           db.session.add(self.user1)
           db.session.commit()
        
        except:
           print("Nose registro el admin")
        

class seedSuperAdmin():
    def __init__(self):
        self.user1=User(
            id_number="123456789",
            name="superAdmin",
            last_name="superAdmin",
            email='correo@superadmin.com',
            date_birth=date(2000,1,1),
            user_name='superadmin',
            pasword=generate_password_hash('superadmin'),
            is_enable=True,
            role_id=1)
        
    def seed(self):
        try:
           db.session.add(self.user1)
           db.session.commit()
        
        except:
           print("Nose registro el superadmin")
        
       
       
       
class seedClient():
    def __init__(self):
        self.user1=User(
            id_number="12345",
            name="user",
            last_name="superAdmin",
            email='correo@user.com',
            date_birth=date(2000,1,1),
            user_name='user',
            pasword=generate_password_hash('user'),
            is_enable=True,
            role_id=3)
        
    def seed(self):
        try:
            db.session.add(self.user1)
            db.session.commit()
        
        except:
           print("Nose registro el usuario")
        
      