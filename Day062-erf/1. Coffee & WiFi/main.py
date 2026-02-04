from flask import Flask, render_template
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
    coffee_rating = SelectField("Coffe Rating", validators=[DataRequired()])
    coffee_rating.choices = [(0,'✘'), (1,'☕️'), (2,'☕️☕️'), (3,'☕️☕️☕️'), (4,'☕️☕️☕️☕️'), (5,'☕️☕️☕️☕️☕️')]
    wifi_rating = SelectField("Wifi Rating", validators=[DataRequired()])
    wifi_rating.choices = [(0,'✘'), (1,'💪'), (2,'💪💪'), (3,'💪💪💪'), (4,'💪💪💪💪'), (5,'💪💪💪💪💪')]
    power_rating = SelectField("Power Rating", validators=[DataRequired()])
    coffee_rating.choices = [(0,'✘'), (1,'🔌'), (2,'🔌🔌'), (3,'🔌🔌🔌'), (4,'🔌🔌🔌🔌'), (5,'🔌🔌🔌🔌🔌')]
    submit = SubmitField('Submit')


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")

@app.route('/add')
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("True")
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)

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
