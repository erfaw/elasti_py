from flask import Flask, render_template
from datetime import datetime as dt
import requests as rq

# Get this year
year = dt.now().date().year

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template("index.html", year=year,)

@app.route('/guess/<name>')
def guess(name):
    params = {"name": name, "country_id": "IR"}
    READ_TIMEOUT = 5
    # API call for gender
    gender_api_link = f"https://api.genderize.io"
    try: 
        res = rq.get(gender_api_link, params,timeout= READ_TIMEOUT)
        res.raise_for_status()
        gender = res.json()['gender']
    except rq.exceptions.RequestException as e:
        gender = 'Error!'
        print(e)
    
    # API call for age
    age_api_link = f"https://api.agify.io"
    try:
        res = rq.get(age_api_link, params, timeout= READ_TIMEOUT)
        res.raise_for_status()
        age = res.json()['age']
    except rq.exceptions.RequestException as e:
        age = 'Error!'
        print(e)

    return render_template("guess.html", year=year, name=name, gender=gender, age=age)

if __name__ == "__main__":
    app.run(debug=True)