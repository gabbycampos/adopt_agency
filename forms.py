from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, FloatField, BooleanField, IntegerField, TextAreaField
from wtforms.validators import InputRequired, Optional, Email, URL, NumberRange

# Pet name
# Species
# Photo URL
# Age
# Notes
# This should be at the URL path /add. Add a link to this from the homepage.

class AddPetForm(FlaskForm):
    name = StringField("Pet Name", validators=[InputRequired(message="Pet Name can't be blank")])
    species = SelectField('Species', choices=[('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')])
    photo = StringField("Photo URL", validators=[Optional(), URL(require_tld=True, message="Should be a vaild URL")])
    age = IntegerField("Age of Pet",validators=[NumberRange(min=0, max=30, message="Age should be between 0 to 30"),Optional()])
    notes = TextAreaField("Notes", validators=[Optional()])
    available = BooleanField("Is Available?")

class EditPetInfo(FlaskForm):
    photo_url = StringField("Photo URL for Pet", validators=[Optional()])
    notes = TextAreaField("Other Notes", validators=[Optional()])
    available = BooleanField("Is Available?")