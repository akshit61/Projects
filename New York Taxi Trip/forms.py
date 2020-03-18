from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, FloatField
from wtforms.fields.html5 import DateTimeLocalField
from wtforms.validators import data_required, NumberRange, InputRequired


class trip_form(FlaskForm):
    passenger_count = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)]
    no_of_passengers = SelectField('# of Passengers', choices=passenger_count, validators=[data_required()])
    dt = DateTimeLocalField('Date', format='%Y-%m-%dT%H:%M', validators=[InputRequired()])
    cab_type = [(1, 1), (2, 2)]
    cab_vendor = SelectField('Cab Vendor', validators=[data_required()], choices=cab_type)
    pickup_longitude = FloatField('Pickup Longitude', validators=[data_required(), NumberRange(max=-69.24891663
                                                                                               , min=-121.9331284)])
    pickup_latitude = FloatField('Pickup Latitude', validators=[data_required(), NumberRange(max=42.81493759
                                                                                             , min=37.3895874
                                                                                             )])
    dropoff_longitude = FloatField('Dropoff Longitude', validators=[data_required(), NumberRange(max=-67.49679565
                                                                                                , min=-121.9333267
                                                                                                )])
    dropoff_latitude = FloatField('Dropoff Latitude', validators=[data_required(), NumberRange(max=48.85759735
                                                                                               , min=36.60132217
                                                                                               )])
    store_and_fwd_flag = SelectField('Store and Forward', choices=[(0, 'No'), (1, 'Yes')],
                                     validators=[data_required()])
    submit = SubmitField('Predict')
