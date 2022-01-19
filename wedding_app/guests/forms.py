from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField, RadioField
from wtforms.validators import DataRequired, Length, Email, ValidationError
from wedding_app.models import Guest


def existing_email_check(self, email):
    guest = Guest.query.filter_by(email=email.data).first()
    if guest:
        raise ValidationError('This email was already added')

class NewGuestForm(FlaskForm):
    name = StringField('Guest Name', 
                       validators=[DataRequired(),
                                   Length(min=2, max=50)])
    email = EmailField('Email', validators=[DataRequired(), Email(), existing_email_check])
    attendance = RadioField('Attendance',choices=['Yes','Maybe','No'],
                            validators=[DataRequired()])
    save = SubmitField('Save')
    
class GuestForm(FlaskForm):
    name = StringField('Guest Name', 
                       validators=[DataRequired(),
                                   Length(min=2, max=50)])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    attendance = RadioField('Attendance',choices=['Yes','Maybe','No'],
                            validators=[DataRequired()])
    save = SubmitField('Save')
    
class RSVPForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Submit')