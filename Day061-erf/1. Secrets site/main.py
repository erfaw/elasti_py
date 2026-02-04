from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap5

# Build class for login form
class LoginForm(FlaskForm):
    email = EmailField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8)])
    submit=  SubmitField(label='Log In')

app = Flask(__name__)
app.secret_key = "nothingImportantForNow"

bootstrap = Bootstrap5(app)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    # Build a login form obj
    login_form = LoginForm()
    # If 'POST'
    if request.method == 'POST':
        # Check if validation was alright
        if login_form.validate_on_submit():
            # Check for adminstrator access
            if login_form.email.data == 'admin@email.com' and login_form.password.data == '12345678':
                # Return admin page
                return render_template("success.html")
            else:
                # Otherwise return Denied page
                return render_template("denied.html")
        # Must be some issue with entry values
        else:
            # Return normal page with errors
            return render_template(
            "login.html",
            form= login_form
            )
    elif request.method == 'GET':
        # If 'GET': render normal page
        return render_template(
            "login.html",
            form= login_form
        )


if __name__ == '__main__':
    app.run(debug=True)
