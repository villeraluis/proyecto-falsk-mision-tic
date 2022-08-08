from utils.db import db

class Client(db.Model):
    __tablename__ = 'clients'
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(50),nullable=False)
    phone = db.Column(db.String(20),nullable=False)
    user_id = db.Column(db.String(20), db.ForeignKey('users.id_number'),nullable=False)

    