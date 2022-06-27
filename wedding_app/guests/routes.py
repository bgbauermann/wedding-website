from flask import render_template, flash, url_for, redirect, request, abort, Blueprint
from wedding_app import db
from wedding_app.guests.forms import RSVPForm, GuestForm, NewGuestForm
from wedding_app.models import Guest
from flask_login import login_user, logout_user, current_user, login_required

guests = Blueprint('guests', __name__)

@guests.route('/rsvp', methods=['GET','POST'])
def rsvp():
    if current_user.is_authenticated:
        return redirect(url_for('guests.list_guests'))
    form = RSVPForm()
    if form.validate_on_submit():
        guest = Guest.query.filter_by(email=form.email.data).first()
        if not guest:
            guest = Guest(email=form.email.data,
                          guest_group=form.email.data)
            db.session.add(guest)
            db.session.commit()
            login_user(guest)
            return redirect(url_for('guests.edit_guest', guest_id=guest.id))
        login_user(guest)
        return redirect(url_for('guests.list_guests'))
    return render_template('rsvp.html', form=form)

@guests.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.home'))

@guests.route('/guests', methods=['GET','POST'])
@login_required
def list_guests():
    group = current_user.guest_group
    guests = Guest.query.filter_by(guest_group=group)
    return render_template('guests.html', guests=guests)


@guests.route('/add_guest', methods=['GET','POST'])
@login_required
def add_guest():
    guest_count = Guest.query.filter_by(guest_group=current_user.guest_group).count()
    if guest_count >= 6:
        flash("You've reached the maximum number of guests.", "is-danger")
        return redirect(url_for('guests.list_guests'))
    form = NewGuestForm()
    if form.validate_on_submit():
        new_guest = Guest(name=form.name.data,
                          email=form.email.data,
                          attendance=form.attendance.data,
                          menu = form.menu.data,
                          guest_group=current_user.email)
        db.session.add(new_guest)
        db.session.commit()
        return redirect(url_for('guests.list_guests'))
    return render_template('guest-details.html', form=form, email_edit=True)


@guests.route('/delete_guest/<int:guest_id>', methods=['POST'])
@login_required
def delete_guest(guest_id):
    guest = Guest.query.get_or_404(guest_id)
    if (guest.email != current_user.email) and (guest.guest_group != current_user.email):
        abort(403)
    else:
        db.session.delete(guest)
        db.session.commit()
    return redirect(url_for('guests.list_guests'))


@guests.route('/guests/<int:guest_id>', methods=['GET','POST'])
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
        guest.menu = form.menu.data
        db.session.commit()
        return redirect(url_for('guests.list_guests'))
    if request.method == 'GET':
        form.name.data = guest.name
        form.email.data = guest.email
        form.attendance.data = guest.attendance
        form.menu.data = guest.menu
    return render_template('guest-details.html', form=form)