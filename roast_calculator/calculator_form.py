from flask_wtf import FlaskForm
from wtforms.fields.html5 import TimeField
from wtforms import SubmitField
from wtforms.validators import InputRequired


class CalculatorForm(FlaskForm):
    meat_in_time = TimeField('meat in time',
                               [InputRequired()])
    meat_cooking_duration = TimeField('meat cooking duration',
                                      [InputRequired()])

    submit = SubmitField('Submit')
