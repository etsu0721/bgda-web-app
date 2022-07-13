from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

# Class: SignUpForm inheriting from FlaskForm
class SignUpForm(FlaskForm):
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
    email = StringField(
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
    submit =  SubmitField(label='Sign Up')

# Class: SignInForm inheriting from FlaskForm
class SignInForm(FlaskForm):
    email = StringField(
        'Email',
        validators=[DataRequired(), Email()]
    )
    password = PasswordField(
        'Password', 
        validators=[DataRequired(), Length(6, 20, message='Password must be between 6 and 20 characters')]
    )
    # Allow user to stay signed in for sometime on browser close
    remember = BooleanField('Remeber me')
    submit =  SubmitField(label='Sign In')