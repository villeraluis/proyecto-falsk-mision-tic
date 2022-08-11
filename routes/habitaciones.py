from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.room import Room
from utils.db import db
from forms.roomForm import RoomForm
from flask_login import login_user as login_flask, current_user, logout_user, login_required
from datetime import date

habitaciones = Blueprint("habitaciones", __name__)

@habitaciones.route('/admin')
@login_required
def index_admin():
    today = date.today() 
    rooms= Room.query.all()
    return render_template('habitaciones/indexAdmin.html',rooms=rooms,today=today)


@habitaciones.route('/crear_admin',methods=['GET','POST'])
@login_required
def create():
    form = RoomForm()
    if form.validate_on_submit():
        number=form.number.data
        description=form.description.data
        
        new_room = Room()
        new_room.number=number
        new_room.description=description
        
        db.session.add(new_room)
        db.session.commit()

        flash('Habitacion Creada Correctamente!')
        
        return redirect(url_for('habitaciones.index_admin'))
                        
    return render_template('habitaciones/create.html',form=form)



@habitaciones.route("/actualizar_admin/<id>", methods=["GET", "POST"])
@login_required
def update(id):
    
    room = Room.query.get(id)
    form = RoomForm(obj=room)

    if form.validate_on_submit():
        number=form.number.data
        description=form.description.data
        is_enable=form.is_enable.data
        room.is_enable=is_enable
        room.number=number
        room.description=description
        
        db.session.commit()

        flash('Habitacion Actualizada Correctamente!')
        
        return redirect(url_for('habitaciones.index_admin'))
                        
    return render_template('habitaciones/update.html',form=form, id=id)


@habitaciones.route('/ver_habitacion_admin/<id>',methods=['GET'])
@login_required
def show_admin(id):
    room = Room.query.get(id)            
    return render_template('habitaciones/showAdmin.html',room=room)


@habitaciones.route("/borrar_admin/<id>", methods=["GET"])
@login_required
def disable(id):
    room = Room.query.get(id)  
    room.is_enable=False
    db.session.commit()
    flash('Habitacion desabilitada Correctamente!')
    
    return redirect(url_for('habitaciones.index_admin'))


@habitaciones.route('/users')
@login_required
def index_users():
    users = Room.query.all() 
    return render_template('viewsAdmin/indexRooms.html',users=users)


