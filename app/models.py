from . import db
from werkzeug.security import generate_password_hash
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import TextAreaField,PasswordField,SelectField
from wtforms.validators import DataRequired
from wtforms.validators import Email
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import InputRequired




 

class Users(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` or some other name.
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80))
    lastname = db.Column(db.String(80))
    gender=db.Column(db.String(80))
    email=db.Column(db.String(150))
    password = db.Column(db.String(255))

    def __init__(self, firstname, lastname,gender,email, password):
        self.firstname = firstname
        self.lastname = lastname
        self.gender=gender
        self.email=email
        self.password = generate_password_hash(password, method='pbkdf2:sha256')

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' %  self.email