from app import app, db
from flask import Flask, url_for, render_template, flash, redirect
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Staff, new_registration
from app.forms import RegistrationForm
from app.forms import LoginForm
from app.forms import AddStaffForm
from app.forms import EditStaffForm
from werkzeug.urls import url_parse
from flask import send_from_directory
from sqlalchemy import exc

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

@app.route('/add_staff', methods=['GET', 'POST'])
@login_required
def add_staff():
    form = AddStaffForm()
    if form.validate_on_submit():
        staff = Staff(staff_id=form.staff_id.data, name=form.name.data, ip=form.ip.data, mac=form.mac.data, method=form.method.data)
        try:
            db.session.add(staff)
            db.session.commit()
            flash('Congratulations, you have added the staff!')
        except exc.IntegrityError:
            db.session.rollback()
            flash('Could not add the staff, repeated values!')
        return redirect(url_for('add_staff'))
    return render_template('add.html', title='Add Staff', form=form)

@app.route('/staff_list', methods=['GET'])
@login_required
def staff_list():
    staffs = Staff.query.all()
    #pls ignore the fact that staff is the plural of staff -_-
    return render_template('list.html', title='Staff List', staffs=staffs)

@app.route('/staff_edit/<int:staff_id>', methods=['GET', 'POST'])
@login_required
def staff_edit(staff_id):
    staff = Staff.query.filter_by(staff_id=staff_id).first()
    if staff is None:
        flash('Staff does not exist')
        return redirect(url_for('staff_list'))
    form = EditStaffForm(obj=staff)
    if form.validate_on_submit():
        staff.staff_id = form.staff_id.data
        staff.name = form.name.data
        staff.ip = form.ip.data
        staff.mac = form.mac.data
        staff.method = form.method.data
        try:
            db.session.add(staff)
            db.session.commit()
            flash('The staff has been updated!')
        except exc.IntegrityError:
            db.session.rollback()
            flash('Could not update the staff, repeated values!')
        return redirect(url_for('staff_edit', staff_id=staff.staff_id))
    return render_template('edit.html', title='Editing Staff', form=form, staff=staff)

@app.route('/staff_delete/<int:staff_id>', methods=['GET'])
@login_required
def staff_delete(staff_id):
    staff = Staff.query.filter_by(staff_id=staff_id).first()
    if staff is None:
        flash('Staff does not exist')
        return redirect(url_for('staff_list'))
    Staff.query.filter(Staff.staff_id == staff.staff_id).delete()
    db.session.commit()
    flash('Staff deleted successfully')
    return redirect(url_for('staff_list'))