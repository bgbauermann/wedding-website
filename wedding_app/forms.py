from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField, RadioField
from wtforms.validators import DataRequired, Length, Email

class GuestForm(FlaskForm):
    name = StringField('Guest Name', 
                       validators=[DataRequired(),
                                   Length(min=2, max=50)])
    email = EmailField('Email',
                       validators=[DataRequired(),
                                    Email()])
    submit = SubmitField('Submit')

    
class GuestDetailsForm(FlaskForm):
    
    name = StringField('Guest Name', 
                       validators=[DataRequired(),
                                   Length(min=2, max=50)])
    email = EmailField('Email',
                       validators=[DataRequired(),
                                    Email()])
    attendance = RadioField('Attendance',choices=['Yes','Maybe','No'])
    menu = RadioField('Menu', choices=['Beef','Chicken'])
    transportation = RadioField('Transportation', choices=['Yes','No'])
    
    save = SubmitField('Save')