# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 13:46:02 2021

@author: bgbau
"""

from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField
from wtforms.validators import DataRequired, Length, Email

class GuestForm(FlaskForm):
    name = StringField('Guest Name', 
                       validators=[DataRequired(),
                                   Length(min=2, max=50)])
    email = EmailField('Email',
                       validators=[DataRequired(),
                                    Email()])
    submit = SubmitField('Register')
    
class GuestDetailsForm(FlaskForm):
    attendance = 0
    transportation = 0
    menu = 0
    submit = SubmitField('Save')