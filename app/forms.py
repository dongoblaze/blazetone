from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField,SelectField,TextAreaField
from wtforms.validators import InputRequired,DataRequired, Email
from flask_wtf.file import FileField, FileRequired, FileAllowed


class UserRegistration(FlaskForm):
 firstname = StringField('First Name', validators=[DataRequired()])
 lastname = StringField('Last Name', validators=[DataRequired()])
 gender = SelectField('Gender', choices=[('Male', 'Male'), ('Female', 'Female')])
 email = StringField('Email', validators=[DataRequired(), Email()])
 password= PasswordField("Password", validators=[InputRequired()])

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')