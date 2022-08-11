from pydoc import cli
from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.client import Client
from models.user import User
from utils.db import db
from werkzeug.security import (generate_password_hash)
from flask_login import login_user as login_flask, current_user, logout_user, login_required
from forms.userForm import UserForm,ClientForm
from app import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

admin = Blueprint("admin", __name__)

@admin.route('/')
def index():  
    return render_template('viewsAdmin/index.html')

@admin.route('/register_user',methods=['GET','POST'])
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
        role_id=2
        
        
        if User.query.filter_by(user_name=user_name).first():
            print ("el nombre de usuario ya se uso antes")
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
            flash('Cuenta Creada Correctamente!')

        return redirect(url_for('admin.index_users'))
                        
    return render_template('auth/registerUserForAdmin.html',form=form,formCli=formCli)


@admin.route('/register_admin',methods=['GET','POST'])
def register_admin():
    form = UserForm()
    if form.validate_on_submit():
        id_number=form.id_number.data
        name=form.name.data
        last_name=form.last_name.data
        email=form.email.data
        date_birth = form.date_birth.data
        user_name=form.user_name.data
        pasword=form.pasword.data
        role_id=1

        if User.query.filter_by(user_name=user_name).first():
            print ("el nombre de usuario ya se uso antes")
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
            
            flash('Cuenta Creada Correctamente!')
            return redirect(url_for('admin.index_users'))
              
    return render_template('auth/registerAdmin.html',form=form)

@admin.route('/users')
def index_users():
    users = User.query.all()  
    return render_template('viewsAdmin/indexUsers.html',users=users)
            
@admin.route("/actualizar_usuario/<id>", methods=["GET", "POST"])
def update(id):
    # get contact by Id
    print(id)
    contact = Contact.query.get(id)

    if request.method == "POST":
        contact.fullname = request.form['fullname']
        contact.email = request.form['email']
        contact.phone = request.form['phone']

        db.session.commit()

        flash('Contact updated successfully!')

        return redirect(url_for('contacts.index'))

    return render_template("update.html", contact=contact)


@admin.route("/borrar_usuario/<id>", methods=["GET"])
def delete_user(id):
    reservation = User.query.get(id) 
    if reservation.role_id==2:
        cliente= Client.query.filter_by(user_id=id).first()    
        db.session.delete(cliente)
        db.session.commit()
        flash('cliente Borrado Correctamente!')
       
    db.session.delete(reservation)
    db.session.commit()
    
    flash('Usuario Borrado Correctamente!')
    
    return redirect(url_for('admin.index_users'))
