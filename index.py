from app import app
from models.seedRoles import seedRoles

from utils.db import db

with app.app_context():
    db.create_all()
    #seedRoles().seed()
   
    

if __name__ == '__main__':
    app.run(debug=True)
