# -*- coding: utf-8 -*-

from flask import Flask, render_template, flash, url_for, redirect
from forms import GuestForm, GuestDetailsForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'as9fdsg8ab73pfbbsv708zs0'

guest_info = {
                 'name': 'Joao',
                 'attendance': 'Yes',
                 'transportation': 'Yes',
                 'menu': 'Beef',
            }

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', guest_info=guest_info)

@app.route('/rsvp', methods=['GET','POST'])
def rsvp():
    form = GuestForm()
    #if form.validate_on_submit():
        #if user already registered read his saved details
        #otherwise display blank form
    return render_template('rsvp.html', form=form)

@app.route('/guestdetails')
def rsvp_details():
    form = GuestDetailsForm()
    if form.validate_on_submit():
        flash(f'Success! Your choices were saved.', category='success')
        return redirect(url_for('home'))
    return render_template('rsvp.html', form=form)