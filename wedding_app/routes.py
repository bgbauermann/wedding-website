from flask import render_template, flash, url_for, redirect, request, abort
from wedding_app import app, db
from wedding_app.forms import RSVPForm, GuestForm, NewGuestForm
from wedding_app.models import Guest
from flask_login import login_user, logout_user, current_user, login_required

@app.route('/')
@app.route('/home')
def home():
    logout_user()
    return render_template('home.html')


@app.route('/rsvp', methods=['GET','POST'])
def rsvp():
    if current_user.is_authenticated:
        return redirect(url_for('guests'))
    form = RSVPForm()
    if form.validate_on_submit():
        guest = Guest.query.filter_by(email=form.email.data).first()
        if not guest:
            guest = Guest(email=form.email.data,
                          guest_group=form.email.data)
            db.session.add(guest)
            db.session.commit()
            login_user(guest)
            return redirect(url_for('edit_guest', guest_id=guest.id))
        login_user(guest)
        return redirect(url_for('guests'))
    return render_template('rsvp.html', form=form)


@app.route('/guests', methods=['GET','POST'])
@login_required
def guests():
    group = current_user.guest_group
    guests = Guest.query.filter_by(guest_group=group)
    return render_template('guests.html', guests=guests)


@app.route('/add_guest', methods=['GET','POST'])
@login_required
def add_guest():
    guest_count = Guest.query.filter_by(guest_group=current_user.guest_group).count()
    if guest_count >= 5:
        flash("You've reached the maximum number of guests.", "is-danger")
        return redirect(url_for('guests'))
    form = NewGuestForm()
    if form.validate_on_submit():
        new_guest = Guest(name=form.name.data,
                          email=form.email.data,
                          guest_group=current_user.email)
        db.session.add(new_guest)
        db.session.commit()
        return redirect(url_for('guests'))
    return render_template('guest-details.html', form=form, email_edit=True)


@app.route('/delete_guest/<int:guest_id>', methods=['GET','POST'])
@login_required
def delete_guest(guest_id):
    guest = Guest.query.get_or_404(guest_id)
    if (guest.email != current_user.email) and (guest.guest_group != current_user.email):
        abort(403)
    else:
        db.session.delete(guest)
        db.session.commit()
    return redirect(url_for('guests'))


@app.route('/guests/<int:guest_id>', methods=['GET','POST'])
@login_required
def edit_guest(guest_id):
    form = GuestForm()
    guest = Guest.query.get_or_404(guest_id)
    if (guest.email != current_user.email) and (guest.guest_group != current_user.email):
        abort(403)
    if form.validate_on_submit():
        guest.name = form.name.data
        guest.email = form.email.data
        guest.attendance = form.attendance.data
        db.session.commit()
        return redirect(url_for('guests'))
    if request.method == 'GET':
        form.name.data = guest.name
        form.email.data = guest.email
        form.attendance.data = guest.attendance
    return render_template('guest-details.html', form=form)