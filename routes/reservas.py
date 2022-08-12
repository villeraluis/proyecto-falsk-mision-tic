from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.comment import Comment
from models.reservation import Reservation
from flask_login import login_user as login_flask, current_user, logout_user, login_required
from models.room import Room
from models.user import User

from utils.db import db
from forms.reservationForm import ReservationForm, ReservationFormUser

reservas = Blueprint("reservas", __name__)

@reservas.route('/admin')
@login_required
def index_admin():
    reservations = Reservation.query.all()  
    return render_template('reservas/indexAdmin.html',reservations=reservations)

@reservas.route("admin/crear/<idh>", methods=['GET'])      
@reservas.route('admin/crear', methods=['GET','POST'])
@login_required
def create_admin(idh=None):
    form = ReservationForm()
       
    form.room_id.choices = [(room.id, room.number) for room in Room.query.all()]
    form.user_id.choices = [(client.id_number, client.name) for client in User.query.all()]
    
    if(idh is not None):
        form.room_id.default=idh
        form.process()
    
    if form.validate_on_submit():
        date_from=form.date_from.data
        date_to=form.date_to.data
        status='Realizada - Activa'
        room_id=form.room_id.data
        user_id=form.user_id.data
        
        reservation = Reservation()
        reservation.date_from=date_from
        reservation.date_to=date_to
        reservation.status=status
        reservation.room_id=room_id
        reservation.user_id=user_id

        db.session.add(reservation)
        db.session.commit()

        flash('Reserva Creada Correctamente!')

        return redirect(url_for('reservas.index_admin'))
    
    return render_template('reservas/createAdmin.html',form=form)


@reservas.route('/ver_reserva_admin/<id>',methods=['GET'])
@login_required
def show_admin(id):
    reservation = Reservation.query.get(id)  
    diffDate = reservation.date_to - reservation.date_from             
    return render_template('reservas/showAdmin.html',reservation=reservation,diffDate=diffDate)



@reservas.route("admin/actualizar/<id>", methods=["GET", "POST"])
@login_required
def update_admin(id):
    reservation = Reservation.query.get(id)
    form = ReservationForm(obj=reservation)

    form.room_id.choices = [(room.id, room.number) for room in Room.query.all()]
    form.user_id.choices = [(client.id_number, client.name) for client in User.query.all()]
    
    if form.validate_on_submit():
        date_from=form.date_from.data
        date_to=form.date_to.data
        status='Editada - Activa'
        room_id=form.room_id.data
        user_id=form.user_id.data
        
        reservation.date_from=date_from
        reservation.date_to=date_to
        reservation.status=status
        reservation.room_id=room_id
        reservation.user_id=user_id

        db.session.commit()

        flash('Reserva Actualizada Correctamente!')

        return redirect(url_for('reservas.index_admin'))
                        
    return render_template('reservas/updateAdmin.html',form=form, id=id)



@reservas.route("/borrar_admin/<id>", methods=["GET"])
@login_required
def delete_admin(id):
    reservation = Reservation.query.get(id) 
     
    db.session.delete(reservation)
    db.session.commit()
    flash('Reserva Borrada Correctamente!')
    
    return redirect(url_for('reservas.index_admin'))


@reservas.route('/user')
@login_required
def index_user():  
    reservations = Reservation.query.filter(Reservation.user_id== current_user.id_number).all()
    labelCurrent='Mis Reservas'
    return render_template('reservas/indexUser.html',labelCurrent=labelCurrent,reservations=reservations)


@reservas.route("/crear/<idh>", methods=['GET'])      
@reservas.route('/crear', methods=['GET','POST'])
@login_required
def create_user(idh=None):
    form = ReservationFormUser()
       
    form.room_id.choices = [(room.id, room.number) for room in Room.query.all()]
    
    if(idh is not None):
        form.room_id.default=idh
        form.process()
    
    if form.validate_on_submit():
        date_from=form.date_from.data
        date_to=form.date_to.data
        status='Realizada - Activa'
        room_id=form.room_id.data
        
        reservation = Reservation()
        reservation.date_from=date_from
        reservation.date_to=date_to
        reservation.status=status
        reservation.room_id=room_id
        reservation.user_id=current_user.id_number

        db.session.add(reservation)
        db.session.commit()

        flash('Reserva Creada Correctamente!')

        return redirect(url_for('reservas.index_user'))
    
    return render_template('reservas/createUser.html',form=form)


@reservas.route("/actualizar/<id>", methods=["GET", "POST"])
@login_required
def update_user(id):
    reservation = Reservation.query.get(id)
    form = ReservationFormUser(obj=reservation)

    form.room_id.choices = [(room.id, room.number) for room in Room.query.all()]
   
    
    if form.validate_on_submit():
        date_from=form.date_from.data
        date_to=form.date_to.data
        status='Editada - Activa'
        room_id=form.room_id.data

        reservation.date_from=date_from
        reservation.date_to=date_to
        reservation.status=status
        reservation.room_id=room_id
       

        db.session.commit()

        flash('Reserva Actualizada Correctamente!')

        return redirect(url_for('reservas.index_user'))
                        
    return render_template('reservas/updateUser.html',form=form, id=id)


@reservas.route("/cancelar/<id>", methods=["GET"])
@login_required
def cancel_user(id):
    reservation = Reservation.query.get(id) 
     
    reservation.status='Cancelada'
    db.session.commit()
    flash('Reserva  Ha sido cancelada!')
    
    return redirect(url_for('reservas.index_user'))


@reservas.route('/detalles_reserva/<id>',methods=['GET'])
@login_required
def show_user(id):
    reservation = Reservation.query.get(id) 
    comments= Comment.query.filter(Comment.reservation_id==id).all() 
    diffDate = reservation.date_to - reservation.date_from             
    return render_template('reservas/showUser.html',reservation=reservation,diffDate=diffDate,comments=comments)



@reservas.route('/crear_comentario/<id>', methods=['GET','POST'])
@login_required
def create_cooment_user(id):
    reservation_id=id
    if request.method == 'POST':
        
        description=request.form['description']
        rating=request.form['rating']
        
        
        comment = Comment()
        comment.description=description
        comment.rating=rating
        comment.reservation_id=reservation_id

        db.session.add(comment)
        db.session.commit()

        flash('Comentario Guardado Correctamente!')

        return redirect(url_for('reservas.show_user',id=reservation_id))
    return redirect(url_for('reservas.show_user',id=reservation_id))

@reservas.route('/edidar_comentario/<id>', methods=['GET','POST'])
@login_required
def edit_coment_user(id):
    reservation_id=id
    if request.method == 'POST':
        
        description=request.form['description']
        rating=request.form['rating']
        
        comment = Comment.query.get(request.form['idComment'])
        comment.description=description
        comment.rating=rating
        comment.reservation_id=reservation_id

        db.session.commit()

        flash('Comentario Editado Correctamente!')

        return redirect(url_for('reservas.show_user',id=reservation_id))
    return redirect(url_for('reservas.show_user',id=reservation_id))
    
    
@reservas.route("/borrar_comentario/<id>", methods=["GET",'POST'])
@login_required
def delete_coment_user(id):
    if request.method == 'POST':
        comment = Comment.query.get(request.form['idComment']) 
        
        db.session.delete(comment)
        db.session.commit()
        flash('Coemntario Borrado Correctamente!')
        
        return redirect(url_for('reservas.show_user',id=id))
    return redirect(url_for('reservas.show_user',id=id))
  
   