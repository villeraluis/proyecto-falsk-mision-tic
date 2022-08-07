from models.rol import Rol
from utils.db import db

class seedRoles():
    def __init__(self):
        self.rol1=Rol(description="Administrador")
        self.rol2=Rol(description="Cliente")
        
    def seed(self):
        db.session.add(self.rol1)
        db.session.add(self.rol2)
        db.session.commit()
      