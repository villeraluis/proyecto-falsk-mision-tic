from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.reservation import Reservation
from utils.db import db
from forms.userForm import UserForm

reservas = Blueprint("reservas", __name__)

@reservas.route('/admin')
def index_admin():  
    return render_template('reservas/indexAdmin.html')

       
@reservas.route('admin/crear', methods=['GET','POST'])
def create_admin():
    if request.method == 'POST':
        
        flash('Contact added successfully!')
        return redirect(url_for('contacts.index'))

    return render_template('reservas/createAdmin.html') 


@reservas.route("admin/actualizar/<string:id>", methods=["GET", "PUT"])
def update_admin(id):
    # get contact by Id
    print(id)
   

    if request.method == "POST":
        print (request.form['fullname'])
       

    return render_template("update.html")


@reservas.route("admin/delete", methods=["DELETE"])
def delete(id):
   
    flash('Contact deleted successfully!')

    return redirect(url_for('contacts.index'))




@reservas.route('/user')
def index_user():  
    labelCurrent='Mis Reservas'
    return render_template('reservas/indexUser.html',labelCurrent=labelCurrent)






