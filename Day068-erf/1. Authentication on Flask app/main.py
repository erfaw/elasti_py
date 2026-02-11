from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from sqlalchemy.exc import IntegrityError
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

class User(db.Model):
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
            password= generate_password_hash(request.form['password']),
        )
        try:
            db.session.add(new_user)
            db.session.commit()
            return redirect(
                url_for('secrets', user_logged_id= new_user.id)
            )
        except IntegrityError as e:
            return redirect(
                url_for('register', is_registered_before=True)
            )

    return render_template("register.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/secrets')
def secrets():
    user_id = request.args.get('user_logged_id')
    user_logged = db.get_or_404(User, user_id)
    return render_template(
            "secrets.html",
            user= user_logged,
        )

@app.route('/logout')
def logout():
    pass

@app.route('/download/<path:file_path>')
def download(file_path):
    return send_from_directory(
        'static',
        file_path,
        as_attachment=True,
    )

if __name__ == "__main__":
    app.run(debug=True)
