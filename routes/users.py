from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.client import Client
from models.user import User
from utils.db import db
from forms.userForm import UserForm,ClientForm
from forms.loginForm import Login
from werkzeug.security import (generate_password_hash) 
from flask_login import login_user as login_flask, current_user, logout_user, login_required
from app import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@login_manager.unauthorized_handler
def unauthorized_callback():
    return redirect(url_for('users.login_user'))
   
users = Blueprint("users", __name__)

@users.route('/')
def index():
    return render_template('index.html')


@users.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Se ha Logeado Satisfactoriamente.')
    return redirect(url_for('users.login_user'))


@users.route('/login',methods=['GET','POST'])
def login_user():
    form = Login() 
    if form.validate_on_submit():
        user_name=form.user_name.data
        pasword=form.pasword.data
        
        user=User.query.filter_by(user_name=user_name).first()
        if user and user.check_password(pasword):
            login_flask(user,remember=True)
            if(user.role_id==2):
                return redirect(url_for('admin.index'))
            return redirect(url_for('users.index'))
        
        msj='Usuario o Contraseña incorrectos'
        
        return render_template('auth/loginUser.html',form=form,msj=msj)
        
    return render_template('auth/loginUser.html',form=form)


@users.route('/register',methods=['GET','POST'])
def register_user():
    form = UserForm()
    formCli=ClientForm()
    if form.validate_on_submit() and formCli.validate_on_submit():
        id_number=form.id_number.data
        name=form.name.data
        last_name=form.last_name.data
        email=form.email.data
        date_birth = form.date_birth.data
        user_name=form.user_name.data
        pasword=form.pasword.data
        role_id=3
        
        if User.query.filter_by(user_name=user_name).first():
            print ("el nombre de usuario ya se uso antes")
            
        if User.query.filter_by(id_number=id_number).first():
            print ("el numero de usuario ya se encuentra registrado")
            
        if User.query.filter_by(email=email).first():
            print ("el email del usuario ya se encuentra registrado")
        else:
            new_user = User()
            new_user.id_number=id_number
            new_user.name=name
            new_user.last_name=last_name
            new_user.email=email
            new_user.date_birth=date_birth
            new_user.user_name=user_name
            new_user.pasword= generate_password_hash(pasword)
            new_user.role_id=role_id

            # guardar datos en la tabla usuarios
            db.session.add(new_user)
            db.session.commit()
            
            #datos del cliente
            address=formCli.address.data
            phone=formCli.phone.data
            user_id=id_number
            
            new_client = Client()
            new_client.address=address
            new_client.phone=phone
            new_client.user_id=user_id
            
            
            # guardar datos en la tabla clientes
            db.session.add(new_client)
            db.session.commit()
            
            #login_flask(new_user, remember=True)
        
        
        flash('Cuenta Creada Correctamente!')

        return redirect(url_for('users.index'))
            

        
                        
    return render_template('auth/registerUser.html',form=form,formCli=formCli)








