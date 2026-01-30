from flask import Flask, render_template
from datetime import datetime as dt

# Get this year
year = dt.now().date().year

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template("index.html", year=year,)

if __name__ == "__main__":
    app.run(debug=True)