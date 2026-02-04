from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField, TimeField, SelectField
from wtforms.validators import DataRequired, URL
import csv
from pathlib import Path
import pandas as pd

root_dir = Path(__file__).resolve().parent

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

bootstrap = Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location_url = URLField('Location URL', validators=[DataRequired(), URL()])
    open_time = TimeField('Open time', validators=[DataRequired(),])
    close_time = TimeField('Close time', validators=[DataRequired(),])
    # Rating fields
    coffee_rating = SelectField("Coffe Rating", validators=[DataRequired()], choices=[])
    wifi_rating = SelectField("Wifi Rating", validators=[DataRequired()], choices=[])
    power_rating = SelectField("Power Rating", validators=[DataRequired()], choices=[])
    submit = SubmitField('Submit')


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")

@app.route('/add', methods=["POST", "GET"])
def add_cafe():
    # Build form
    form = CafeForm()

    # Initialize choices attribute for each Rating Field
    form.coffee_rating.choices = [(0,'✘'), (1,'☕️'), (2,'☕️☕️'), (3,'☕️☕️☕️'), (4,'☕️☕️☕️☕️'), (5,'☕️☕️☕️☕️☕️')]
    form.wifi_rating.choices = [(0,'✘'), (1,'💪'), (2,'💪💪'), (3,'💪💪💪'), (4,'💪💪💪💪'), (5,'💪💪💪💪💪')]
    form.power_rating.choices = [(0,'✘'), (1,'🔌'), (2,'🔌🔌'), (3,'🔌🔌🔌'), (4,'🔌🔌🔌🔌'), (5,'🔌🔌🔌🔌🔌')]

    # If was POST
    if request.method == "POST":
        # IF was the form validate correctly
        if form.validate_on_submit():
            # Get new Record
            form_get_data = pd.DataFrame(request.form, index=pd.RangeIndex(1))
            form_get_data = form_get_data.drop(columns=['csrf_token', 'submit'])

            # Update csv file with new data
            prev_csv = pd.read_csv(root_dir/'cafe-data.csv')
            prev_csv.loc[len(prev_csv)+1] = form_get_data.values.tolist()[0]
            prev_csv.to_csv(root_dir/'cafe-data.csv', mode='w', index=False, header= False)

            return redirect(
                url_for('add_cafe',  is_submited=True)
            )
        else: 
            return render_template('add.html', form=form)
    elif request.method == "GET":
        return render_template('add.html', form=form)
    
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    

@app.route('/cafes')
def cafes():
    # Load CSV file using pd
    cafes_df = pd.read_csv(root_dir/'cafe-data.csv')

    # Prepare data to render a table
    table_heads = cafes_df.columns.tolist()
    table_records = cafes_df.values.tolist()

    return render_template(
        'cafes.html', 
        table_heads= table_heads, 
        table_records= table_records
        )

if __name__ == '__main__':
    app.run(debug=True)
