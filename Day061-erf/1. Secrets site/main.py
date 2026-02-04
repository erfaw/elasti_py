from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    email = EmailField(label='Email', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit=  SubmitField(label='Log In')

app = Flask(__name__)
app.secret_key = "nothingImportantForNow"

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login")
def login():
    return render_template(
        "login.html",
        form= LoginForm()
    )


if __name__ == '__main__':
    app.run(debug=True)
