from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetInfo
from wtforms.validators import ValidationError

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'adoptionsecretkey'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.route('/')
def home_page():
    """ Displays Pets """
    pets = db.session.query(Pet).all()
    return render_template('home.html', pets=pets)

@app.route('/pets/add', methods=["GET", "POST"])
def add_pet():
    """ Renders pet form (GET) or handles pet form submission (POST)"""
    form = AddPetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo = form.photo.data
        age = form.age.data
        notes = form.notes.data
        is_available = form.available.data

        pet = Pet(name=name, species=species, photo_url=photo, age=age, notes=notes, available=is_available)
        db.session.add(pet)
        db.session.commit()
        return redirect('/')

    return render_template('add_pet.html', form=form)

@app.route('/pets/<int:pet_id>', methods=["GET","POST"])
def show_pet(pet_id):
    """Display pet details or edit pet """
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetInfo(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.commit()
        return redirect('/')
    return render_template('display_pet.html', pet=pet, form=form)