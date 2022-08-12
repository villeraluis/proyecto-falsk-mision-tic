from flask import Flask

from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_login import login_user as login_flask, current_user, logout_user, login_required


from config import DATABASE_CONNECTION_URI

app = Flask(__name__)


# settings
app.secret_key = 'mysecret'
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_CONNECTION_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# no cache
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

CSRFProtect(app)
SQLAlchemy(app)
login_manager=LoginManager(app)


from routes.users import users
from routes.admin import admin
from routes.habitaciones import habitaciones
from routes.reservas import reservas
app.register_blueprint(users, url_prefix="/")
app.register_blueprint(admin, url_prefix="/admin")
app.register_blueprint(habitaciones, url_prefix="/habitaciones")
app.register_blueprint(reservas, url_prefix="/reservas")

@app.before_request
def middleware():
    print('Antes de la peticion')
    
    