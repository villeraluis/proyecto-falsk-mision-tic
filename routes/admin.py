from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.user import User
from utils.db import db
from forms.userValidatorForm import createUser

admin = Blueprint("admin", __name__)

@admin.route('/')
def index():  
    return render_template('viewsAdmin/index.html')


@admin.route('/register_user',methods=['GET','POST'])
def register_user():
    form = createUser()
    if form.validate_on_submit():
        id_number=form.id_number.data
        name=form.name.data
        last_name=form.last_name.data
        email=form.email.data
        date_birth = form.date_birth.data
        user_name=form.user_name.data
        pasword=form.pasword.data
        
        
        new_user = User(id_number, name, last_name, email, date_birth, user_name, pasword)
        
        # save the object into the database
        db.session.add(new_user)
        db.session.commit()

        flash('Cuenta Creada Correctamente!')

        return redirect(url_for('users.index'))
                        
    return render_template('auth/registerUserForAdmin.html',form=form)

@admin.route('/users')
def index_users():
    users = User.query.all()
    
    return render_template('viewsAdmin/indexUsers.html',users=users)
    
       
@admin.route('/new', methods=['POST'])
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


@admin.route("/update/<string:id>", methods=["GET", "POST"])
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


@admin.route("/delete/<id>", methods=["GET"])
def delete(id):
    contact = Contact.query.get(id)
    db.session.delete(contact)
    db.session.commit()

    flash('Contact deleted successfully!')

    return redirect(url_for('contacts.index'))


