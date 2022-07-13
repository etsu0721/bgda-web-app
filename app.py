from datetime import datetime as dt
from flask import Flask, render_template, url_for, flash, redirect
from sqlalchemy import ForeignKey
from forms import SignInForm, SignUpForm
from flask_sqlalchemy import SQLAlchemy

# __name__ is just the name of the module: __main__
app = Flask(__name__)
app.config['SECRET_KEY'] = '08c01258226aaa63532af39e9b8acc72'

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://etsu_conn:vIper sp1/t pretzelz@localhost/bgda_db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/dev-bgda-db.db'
db = SQLAlchemy(app)

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    nickname = db.Column(db.String(20))
    email = db.Column(db.String(50), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"Player('{self.first_name}', '{self.nickname}', '{self.last_name}', '{self.email}')"

class Bar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    address = db.Column(db.String(100), unique=True, nullable=False)
    teams = db.relationship('Team', backref='bar', lazy=True)

    def __repr__(self):
        return f"Bar('{self.name}', '{self.address}')"

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    home_bar_id = db.Column(db.Integer, db.ForeignKey('bar.id'), nullable=False)

    def __repr__(self):
        return f"Team('{self.name}')"

# @app.route('/') is a decorator
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/signup', methods=['GET', 'POST'])
def sign_up():
    form = SignUpForm()
    if form.validate_on_submit():
        # Display one-time success message and redirect to Home page
        flash(
            f'Account created for {form.first_name.data} {form.last_name.data}', 
            'success'
        )
        return redirect(url_for('home'))
    return render_template('sign_up.html', title='Sign Up', form=form)

@app.route('/signin', methods=['GET', 'POST'])
def sign_in():
    form = SignInForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@gmail.com' and form.password.data == 'password':
            # Display one-time success message and redirect to Home page
            flash('Signed in', 'success')
            return redirect(url_for('home'))
        else:
            # Display one-time failure message and redirect back to Sign In page
            flash('Incorrect email or password. Please try again.', 'danger')
    return render_template('sign_in.html', title='Sign In', form=form)

# Enable dev server to show changes without having to restart
if __name__ == '__main__':
    app.run(debug=True)