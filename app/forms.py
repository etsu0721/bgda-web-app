from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import InputRequired, Length, Email, EqualTo, ValidationError, Regexp
from app.models import Player

class RegistrationForm(FlaskForm):
    first_name = StringField(
        'First Name',
        validators=[InputRequired(), Length(max=20, message='Name must be less than 20 characters')]
    )
    last_name = StringField(
        'Last Name',
        validators=[InputRequired(), Length(max=20, message='Name must be less than 20 characters')]
    )
    nickname = StringField(
        'Nickname',
        validators=[Length(max=20, message='Nickname must be less than 20 characters')]
    )
    email  = StringField(
        'Email',
        validators=[InputRequired(), Email()]
    )
    password = PasswordField(
        'Password', 
        validators=[InputRequired(), Length(6, 20, message='Password must be between 6 and 20 characters')]
    )
    confirm_password = PasswordField(
        'Confirm Password', 
        validators=[InputRequired(), EqualTo('password')]
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
        validators=[InputRequired(), Email()]
    )
    password = PasswordField(
        'Password', 
        validators=[InputRequired(), Length(6, 20, message='Password must be between 6 and 20 characters')]
    )
    # Allow user to stay logged in for sometime on browser close
    remember = BooleanField('Remeber me')
    submit =  SubmitField(label='Login')

class UpdateAccountForm(FlaskForm):
    first_name = StringField(
        'First Name',
        validators=[InputRequired(), Length(max=20, message='Name must be less than 20 characters')]
    )
    last_name = StringField(
        'Last Name',
        validators=[InputRequired(), Length(max=20, message='Name must be less than 20 characters')]
    )
    nickname = StringField(
        'Nickname',
        validators=[Length(max=20, message='Nickname must be less than 20 characters')]
    )
    email  = StringField(
        'Email',
        validators=[InputRequired(), Email()]
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

class BarForm(FlaskForm):
    bar_name = StringField('Name', validators=[InputRequired(), Length(max=50, message='Team name must be less than 50 characters.')])
    bar_address = StringField('Address', validators=[InputRequired(), Length(max=255, message='Bar name must be less than 250 characters.')])
    bar_phone = StringField('Phone', validators=[InputRequired(), Regexp('^[0-9]{10}$', message='Phone number must be 10 digits (exclude parentheses, hyphens, spaces, etc.).')])
    submit = SubmitField('Add')

class TeamForm(FlaskForm):
    team_name = StringField('Name', validators=[InputRequired(), Length(max=50, message='Team name must be less than 50 characters')])
    team_captain = SelectField('Captain', validators=[InputRequired()])
    home_bar = SelectField('Home Bar', validators=[InputRequired()])
    submit = SubmitField('Add')