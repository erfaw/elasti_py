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
    # # API call for gender
    # gender_api_link = "https://api.genderize.io/"
    # params = {"name": name}
    # with rq.get(gender_api_link, params=params,) as res:
    #     res.raise_for_status()
    #     content = res.json()
    # print(content)

    return render_template("index.html", year=year, name=name, )

if __name__ == "__main__":
    app.run(debug=True)