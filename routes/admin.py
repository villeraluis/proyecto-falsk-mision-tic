from pydoc import cli
from flask import Blueprint, render_template, request, redirect, url_for, flash
from middlewares.routeMiddleware import adminMiddleware,userMiddleware
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


from datetime import date
def edad_actual(fecha_nacimiento):
    """
    Calcular edad actual basado en fecha de nacimiento
    :return: int edad
    """
    # Obtener fecha de hoy
    today = date.today()
    # Calcular Edad
    age = today.year - fecha_nacimiento.year - (
            (today.month, today.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
    return age


   


    

admin = Blueprint("admin", __name__)

@admin.route('/')
@login_required
@adminMiddleware
def index():  
    return render_template('viewsAdmin/index.html')

@admin.route('/register_user',methods=['GET','POST'])
@login_required
@adminMiddleware
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
@login_required
@adminMiddleware
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
@login_required
@adminMiddleware
def index_users():
    users = User.query.all()  
    return render_template('viewsAdmin/indexUsers.html',users=users)


@admin.route('/ver_usuario_admin/<id>',methods=['GET'])
@login_required
@adminMiddleware
def show_admin(id):
    user = User.query.get(id) 
    edad=edad_actual(user.date_birth)
    if(user.role_id==1):
        return render_template('viewsAdmin/showUserAdminForAdmin.html',user=user,edad=edad)
                     
    return render_template('viewsAdmin/showUserForAdmin.html',user=user,edad=edad)         
  
            
@admin.route("/actualizar_usuario/<id>", methods=["GET", "POST"])
@login_required
@adminMiddleware
def update_admin(id):
    user = User.query.get(id)
    form = UserForm(obj=user)
    if(user.role_id==1):
        if form.validate_on_submit():
            id_number=form.id_number.data
            name=form.name.data
            last_name=form.last_name.data
            email=form.email.data
            date_birth = form.date_birth.data
            user_name=form.user_name.data
            pasword=form.pasword.data
            is_enable=form.is_enable.data
    
            user.id_number=id_number
            user.name=name
            user.last_name=last_name
            user.email=email
            user.date_birth=date_birth
            user.user_name=user_name
            user.pasword= generate_password_hash(pasword)
            user.is_enable=is_enable
            
            # guardar datos en la tabla usuarios
            db.session.commit()
        
            flash('Cuenta Actualizada Correctamente!')
            return redirect(url_for('admin.index_users'))
        return render_template('viewsAdmin/updateUserAdminForAdmin.html',form=form, id=id)
    
    
    client=Client.query.filter_by(user_id=id).first()
    formCli=ClientForm(obj=client)

    if form.validate_on_submit():
        id_number=form.id_number.data
        name=form.name.data
        last_name=form.last_name.data
        email=form.email.data
        date_birth = form.date_birth.data
        user_name=form.user_name.data
        pasword=form.pasword.data
        is_enable=form.is_enable.data
 
        user.id_number=id_number
        user.name=name
        user.last_name=last_name
        user.email=email
        user.date_birth=date_birth
        user.user_name=user_name
        user.pasword= generate_password_hash(pasword)
        user.is_enable=is_enable
        
        # guardar datos en la tabla usuarios
        db.session.commit()
        
         #datos del cliente
        address=formCli.address.data
        phone=formCli.phone.data
        user_id=id_number
            
            
        client.address=address
        client.phone=phone
        client.user_id=user_id
     
        # guardar datos en la tabla clientes       
        db.session.commit()
            
        flash('Cuenta Actualizada Correctamente!')
        return redirect(url_for('admin.index_users'))
        
        
                        
    return render_template('viewsAdmin/updateUserForAdmin.html',form=form,formCli=formCli, id=id)



@admin.route("/desabilitar_usuario/<id>", methods=["GET"])
@login_required
@adminMiddleware
def disable_user(id):
    user = User.query.get(id) 
    user.is_enable = False  
    db.session.commit()
    
    flash('Usuario desabilitado Correctamente!')
    
    return redirect(url_for('admin.index_users'))
