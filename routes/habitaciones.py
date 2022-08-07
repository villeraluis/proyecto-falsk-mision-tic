from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.room import Room
from utils.db import db
from forms.userValidatorForm import createRoom

habitaciones = Blueprint("habitaciones", __name__)

@habitaciones.route('/')
def index():  
    return render_template('viewsAdmin/index.html')


@habitaciones.route('/register_user',methods=['GET','POST'])
def register_user():
    form = createRoom()
    if form.validate_on_submit():
        id_number=form.id_number.data
        name=form.name.data
        last_name=form.last_name.data
        email=form.email.data
        date_birth = form.date_birth.data
        user_name=form.user_name.data
        pasword=form.pasword.data
        
        
        new_user = Room(id_number, name, last_name, email, date_birth, user_name, pasword)
        
        # save the object into the database
        db.session.add(new_user)
        db.session.commit()

        flash('Cuenta Creada Correctamente!')

        return redirect(url_for('users.index'))
                        
    return render_template('auth/registerRoomForAdmin.html',form=form)

@habitaciones.route('/users')
def index_users():
    users = Room.query.all()
    
    return render_template('viewsAdmin/indexRooms.html',users=users)
    
       
@habitaciones.route('/new', methods=['POST'])
def add_contact():
    if request.method == 'POST':

        # receive data from the form
        fullname = request.form['fullname']
        email = request.form['email']
        phone = request.form['phone']

        # create a new Contact object
        new_contact = Contact(fullname, email, phone)

        # save the object into the database
        db.session.add(new_contact)
        db.session.commit()

        flash('Contact added successfully!')

        return redirect(url_for('contacts.index'))


@habitaciones.route("/update/<string:id>", methods=["GET", "POST"])
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


@habitaciones.route("/delete/<id>", methods=["GET"])
def delete(id):
    contact = Contact.query.get(id)
    db.session.delete(contact)
    db.session.commit()

    flash('Contact deleted successfully!')

    return redirect(url_for('contacts.index'))


