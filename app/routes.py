from flask import render_template, url_for, flash, redirect
from app import app
from app.forms import SignInForm, SignUpForm
from app.models import Player, Team, Bar

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
