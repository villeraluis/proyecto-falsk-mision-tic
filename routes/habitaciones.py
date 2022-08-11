from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.room import Room
from utils.db import db
from forms.roomForm import RoomForm

habitaciones = Blueprint("habitaciones", __name__)

@habitaciones.route('/admin')
def index_admin(): 
    rooms= Room.query.all()
    return render_template('habitaciones/indexAdmin.html',rooms=rooms)


@habitaciones.route('/crear_admin',methods=['GET','POST'])
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
def update(id):
    
    room = Room.query.get(id)
    form = RoomForm(obj=room)

    if form.validate_on_submit():
        number=form.number.data
        description=form.description.data
    
        room.number=number
        room.description=description
        
        db.session.commit()

        flash('Habitacion Actualizada Correctamente!')
        
        return redirect(url_for('habitaciones.index_admin'))
                        
    return render_template('habitaciones/update.html',form=form, id=id)


@habitaciones.route('/ver_habitacion_admin/<id>',methods=['GET'])
def show_admin(id):
    room = Room.query.get(id)            
    return render_template('habitaciones/showAdmin.html',room=room)


@habitaciones.route("/borrar_admin/<id>", methods=["GET"])
def delete(id):
    room = Room.query.get(id)  
    db.session.delete(room)
    db.session.commit()
    flash('Habitacion Borrada Correctamente!')
    
    return redirect(url_for('habitaciones.index_admin'))


@habitaciones.route('/users')
def index_users():
    users = Room.query.all() 
    return render_template('viewsAdmin/indexRooms.html',users=users)


