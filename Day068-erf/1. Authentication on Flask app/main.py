from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from sqlalchemy.exc import IntegrityError, NoResultFound
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from pathlib import Path
import os
from dotenv import load_dotenv
import datetime as dt

ROOT_DIR = Path(__file__).resolve().parent
(ROOT_DIR / "instance").mkdir(exist_ok= True)
db_path = ROOT_DIR / 'instance' / 'users.db'
db_path.as_posix()

load_dotenv(ROOT_DIR/'.env')

app = Flask(__name__)
app.config['SECRET_KEY'] = f'{os.environ.get('SECRET_KEY')}'
class Base(DeclarativeBase): pass
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
db = SQLAlchemy(model_class=Base)
db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)

class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(150))
    name: Mapped[str] = mapped_column(String(1000))
    def __repr__(self):
        return f"<User: id={self.id}, name={self.name}, email={self.email}>"
    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/register', methods=["POST", "GET"])
def register():
    if request.method == "POST":
        new_user = User(
            name= request.form['name'],
            email= request.form['email'],
            password= generate_password_hash(
                    password= request.form['password'],
                    salt_length= 8,
                    method= "pbkdf2"
                ),
        )
        try:
            db.session.add(new_user)
            db.session.commit()
            login_user(user= new_user)
            return redirect(
                url_for('secrets')
            )
        except IntegrityError as e:
            flash("You've already signed up with that email, Login instead!")
            return redirect(url_for('register'))

    return render_template("register.html")

@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        try:
            user_by_email = db.session.execute(
                db.select(User).where(User.email == email)
            ).scalar_one()
        except NoResultFound: 
            flash("The email doesn't exist, please try again.")
            return redirect(url_for('login'))
        if check_password_hash(
            user_by_email.password,
            password
        ):
            if login_user(user= user_by_email):
                return redirect(url_for('secrets'))
        else:
            flash("Password incorrect, please try again.")
            return redirect(url_for('login'))
    return render_template("login.html")

@app.route('/secrets')
@login_required
def secrets():
    return render_template(
            "secrets.html",
            user= current_user,
        )

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(
        url_for('home')
    )

@app.route('/download/<path:file_path>')
@login_required
def download(file_path):
    return send_from_directory(
        'static',
        file_path,
        as_attachment=True,
    )

@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)

if __name__ == "__main__":
    app.run(debug=True)
