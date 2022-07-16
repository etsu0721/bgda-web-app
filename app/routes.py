from flask import render_template, url_for, flash, redirect, request
from app import app, db, bcrypt
from app.forms import RegistrationForm, LoginForm, UpdateAccountForm
from app.models import Player, Team, Bar
from flask_login import login_user, current_user, logout_user, login_required
import secrets, os
from PIL import Image

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

def save_picture(form_picture):
    # Randomize file name to avoid collision
    random_hex = secrets.token_hex(8)
    _, file_ext = os.path.splitext(form_picture.filename)
    picture_file_name = random_hex + file_ext
    picture_path = os.path.join(app.root_path, 'static/profile-pics', picture_file_name)
    # Resize image
    output_size = (125, 125)
    img = Image.open(form_picture)
    img.thumbnail(output_size)
    # Save resized image
    img.save(picture_path)
    return picture_file_name

@app.route('/account', methods=['GET', 'POST'] )
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
             picture_file = save_picture(form.picture.data)
             current_user.image_file = picture_file
        current_user.first_name = form.first_name.data
        current_user.last_name = form.last_name.data
        current_user.nickname = form.nickname.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account')) # POST-GET redirect pattern
    elif request.method == 'GET':
        form.first_name.data = current_user.first_name
        form.last_name.data = current_user.last_name
        form.nickname.data = current_user.nickname
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile-pics/' + current_user.image_file)
    return render_template('account.html', title='Account', image_file=image_file, form=form)

