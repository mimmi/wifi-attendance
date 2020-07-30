from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, RadioField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

class AddStaffForm(FlaskForm):
    staff_id = IntegerField('Staff ID', validators=[DataRequired()])
    name = StringField('Staff Name', validators=[DataRequired()])
    method = RadioField('Method', choices=[(1,'Ping'), (2,'ARP')], default=1, coerce=int, validators=[DataRequired()])
    ip = StringField('IP Address', validators=[DataRequired()])
    mac = StringField('MAC Address', validators=[DataRequired()])

class EditStaffForm(FlaskForm):
    staff_id = IntegerField('Staff ID', validators=[DataRequired()])
    name = StringField('Staff Name', validators=[DataRequired()])
    method = RadioField('Method', choices=[(1,'Ping'), (2,'ARP')], default=1, coerce=int, validators=[DataRequired()])
    ip = StringField('IP Address', validators=[DataRequired()])
    mac = StringField('MAC Address', validators=[DataRequired()])