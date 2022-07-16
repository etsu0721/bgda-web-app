from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.models import Player

class RegistrationForm(FlaskForm):
    first_name = StringField(
        'First Name',
        validators=[DataRequired(), Length(max=20, message='Name must be less than 20 characters')]
    )
    last_name = StringField(
        'Last Name',
        validators=[DataRequired(), Length(max=20, message='Name must be less than 20 characters')]
    )
    nickname = StringField(
        'Nickname',
        validators=[Length(max=20, message='Nickname must be less than 20 characters')]
    )
    email  = StringField(
        'Email',
        validators=[DataRequired(), Email()]
    )
    password = PasswordField(
        'Password', 
        validators=[DataRequired(), Length(6, 20, message='Password must be between 6 and 20 characters')]
    )
    confirm_password = PasswordField(
        'Confirm Password', 
        validators=[DataRequired(), EqualTo('password')]
    )
    submit =  SubmitField(label='Register')

    def validate_email(self, email):
        """Ensure user supplied email does not already exist in database

        Args:
            email (string): user email address

        Raises:
            ValidationErr: the user supplied email is already associated with an existing account
        """
        player = Player.query.filter_by(email=email.data).first()
        if player != None:
            raise ValidationError('An account with that email already exists. Try logging in with that email or registering a new email.')

class LoginForm(FlaskForm):
    email = StringField(
        'Email',
        validators=[DataRequired(), Email()]
    )
    password = PasswordField(
        'Password', 
        validators=[DataRequired(), Length(6, 20, message='Password must be between 6 and 20 characters')]
    )
    # Allow user to stay logged in for sometime on browser close
    remember = BooleanField('Remeber me')
    submit =  SubmitField(label='Login')

class UpdateAccountForm(FlaskForm):
    first_name = StringField(
        'First Name',
        validators=[DataRequired(), Length(max=20, message='Name must be less than 20 characters')]
    )
    last_name = StringField(
        'Last Name',
        validators=[DataRequired(), Length(max=20, message='Name must be less than 20 characters')]
    )
    nickname = StringField(
        'Nickname',
        validators=[Length(max=20, message='Nickname must be less than 20 characters')]
    )
    email  = StringField(
        'Email',
        validators=[DataRequired(), Email()]
    )
    picture = FileField(
        'Profile Picture', 
        validators=[FileAllowed(['jpg', 'jpeg', 'png'])]
        )
    submit =  SubmitField(label='Update')

    def validate_email(self, email):
        """Ensure user supplied email does not already exist in database

        Args:
            email (string): user email address

        Raises:
            ValidationErr: the user supplied email is already associated with an existing account
        """
        if email.data != current_user.email:
            player = Player.query.filter_by(email=email.data).first()
            if player != None:
                raise ValidationError('An account with that email already exists. Try logging in with that email or registering a new email.')
 