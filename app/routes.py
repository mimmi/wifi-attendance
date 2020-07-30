from app import app, db
from flask import Flask, url_for, render_template, flash, redirect
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, new_registration
from app.forms import RegistrationForm
from app.forms import LoginForm
from werkzeug.urls import url_parse
from flask import send_from_directory

@app.route('/')
@login_required
def index():
    return render_template("index.html", title='WiFi Attendance V1')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if new_registration():
        return redirect(url_for('register'))
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if new_registration() is not True:
        return redirect(url_for('login'))
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/configuration', methods=['GET'])
def configuration():
    return 'Configuration Main'

@app.route('/configuration/commit_time/<int:seconds>', methods=['GET'])
def set_commit_time(seconds):
    return "Setting the commit time to {} seconds".format(seconds)