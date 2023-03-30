from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, validators, IntegerField, SelectMultipleField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from wtforms.fields import DateField

class InfoForm(FlaskForm):
    startdate = DateField('Start Date', format='%Y-%m-%d', validators=(validators.DataRequired(),))
    enddate = DateField('End Date', format='%Y-%m-%d', validators=(validators.DataRequired(),))
    skills = SelectMultipleField('Skills', validators=(validators.DataRequired(),))
    no_of_panelists = IntegerField('', validators=(validators.DataRequired(),))
    submit = SubmitField('Search')