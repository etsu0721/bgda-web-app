from flask import render_template, url_for, flash, redirect, request
from app import app, db, bcrypt
from app.forms import RegistrationForm, LoginForm
from app.models import Player, Team, Bar
from flask_login import login_user, current_user, logout_user, login_required

# @app.route('/') is a decorator
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        # Hash user supplied password
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = Player(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            nickname=form.nickname.data,
            email=form.email.data,
            password=hashed_password
        )
        db.session.add(user)
        db.session.commit()
        flash(f'Your account has been created! You are now able to log in.','success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        # Check if player is in the database
        player = Player.query.filter_by(email=form.email.data).first()
        if player != None and bcrypt.check_password_hash(player.password, form.password.data):
            login_user(player, remember=form.remember.data)
            flash(f'Logged in!', 'success')
            # Direct user to page they were attempting to access before being prompted to login (if applicable)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page != None else redirect(url_for('home'))
        else:
            flash('Login failed. Check email and password.', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
    logout_user()
    flash(f'Logged out!', 'success')
    return redirect(url_for('home'))

@app.route('/account')
@login_required
def account():
    return render_template('account.html', title='Account')

