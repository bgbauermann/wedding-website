
from flask import render_template, flash, url_for, redirect, request
from wedding_app import app, db
from wedding_app.forms import GuestForm, GuestDetailsForm
from wedding_app.models import Guest
from flask_login import login_user, logout_user, current_user, login_required

@app.route('/')
@app.route('/home')
def home():
    logout_user()
    return render_template('home.html')

@app.route('/rsvp', methods=['GET','POST'])
def rsvp():
    form = GuestForm()
    if form.validate_on_submit():
        guest = Guest.query.filter_by(email=form.email.data).first()
        if not guest:
            guest = Guest(name=form.name.data,
                          email=form.email.data)
            db.session.add(guest)
            db.session.commit()
        login_user(guest)
        return redirect(url_for('guest_details'))
    return render_template('rsvp.html', form=form)

@app.route('/guest-details', methods=['GET','POST'])
@login_required
def guest_details():
    form = GuestDetailsForm()
    #Get guests info to populate forms       
    if form.validate_on_submit():
        flash('Success! Your choices were saved.', category='success')
        return redirect(url_for('home'))
    return render_template('guest-details.html', form=form)