import datetime
from flask import Blueprint, render_template, request
from . import calculator_form

bp = Blueprint('calculator', __name__)

@bp.route('/', methods=('GET', 'POST'))
def calculator():
    form = calculator_form.CalculatorForm()

    if form.validate_on_submit():
        meat_in_datetime = datetime.datetime.combine(datetime.date.today(),
                                                     form.meat_in_time.data)

        meat_cooking_duration = datetime.timedelta(hours=form.meat_cooking_duration.data.hour,
                                                   minutes=form.meat_cooking_duration.data.minute)

        times = calculate_times(meat_in_datetime, meat_cooking_duration)

        return render_template('calculator/calculator.html', form=form,
                               times=times)
    return render_template('calculator/calculator.html', form=form,
                           times=[])

def calculate_times(meat_in_time, meat_cooking_duration):
    """There are core assumptions made about the cooking times for vegetables.
    In time there may be config file parameters, CLI arguments or whatever
    which set these. Actually, would be a good opportunity to use a class with
    defaults actually...

    + Potatoes
      - 10 minutes boiling
      - 5 minutes steaming
      - 50 minutes roasting
      - turn at 25 minutes
    + Parsnips
      - 5 minutes boiling
      - 5 minutes steaming
      - 30 minutes roasting
      - turn at 15 minutes
    """

    meat_out_time = meat_in_time + meat_cooking_duration
    potatoes_in_time = meat_out_time - datetime.timedelta(minutes=10)
    potatoes_on_boil_time = meat_out_time - datetime.timedelta(minutes=25)
    potatoes_off_boil_time = meat_out_time - datetime.timedelta(minutes=15)
    potatoes_turn_time = potatoes_in_time + datetime.timedelta(minutes=25)
    # Target serving time is the time when the roast potatoes are done
    serving_time = potatoes_in_time + datetime.timedelta(minutes=50)

    parsnips_on_boil_time = serving_time - datetime.timedelta(minutes=40)
    parsnips_off_boil_time = serving_time - datetime.timedelta(minutes=35)
    parsnips_in_time = serving_time - datetime.timedelta(minutes=30)
    parsnips_turn_time = serving_time - datetime.timedelta(minutes=15)

    times = [['meat in time ', meat_in_time],
             ['meat out time ', meat_out_time],
             ['potatoes in time ', potatoes_in_time],
             ['potatoes on boil time ', potatoes_on_boil_time],
             ['potatoes off boil time ', potatoes_off_boil_time],
             ['potatoes turn time ', potatoes_turn_time],
             ['ready time ', serving_time],
             ['parsnips on boil time ', parsnips_on_boil_time],
             ['parsnips off boil time ', parsnips_off_boil_time],
             ['parsnips in time ', parsnips_in_time],
             ['parsnips turn time ', parsnips_turn_time],
             ]

    sorted_times = sorted(times, key=lambda x: x[1])

    time_strs = []
    for time in sorted_times:
        # time_str = time[0] + time[1].strftime('%H:%M')
        time_str = [time[0], time[1].strftime('%H:%M')]
        time_strs.append(time_str)

    return time_strs
