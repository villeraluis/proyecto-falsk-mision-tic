from app import app
from models.seed import seedAdmin, seedClient, seedRoles, seedSuperAdmin
from flask import Flask, request

from utils.db import db
   
with app.app_context():
    db.create_all()
      

@app.before_first_request
def middleware():
    try:
        seedRoles().seed()
        seedAdmin().seed()
        seedSuperAdmin().seed()
        seedClient().seed()
 
    except:
        print("Nose registro")
    

        
if __name__ == '__main__':
    app.run(debug=True)
