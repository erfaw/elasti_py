from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String
from pathlib import Path
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

class BookEntry(FlaskForm):
    book_name = StringField(label="Book:", validators=[DataRequired(),])
    book_author = StringField(label="Author:", validators= [DataRequired()])
    book_rate = SelectField(label="Rate:", validators= [DataRequired()], choices=[])
    submit = SubmitField('Submit')

class Base(DeclarativeBase): pass

db = SQLAlchemy(model_class= Base)

app = Flask(__name__)

ROOT_DIR = Path(__file__).resolve().parent
(ROOT_DIR / "instance").mkdir(exist_ok=True)
db_path = (ROOT_DIR/"instance"/"library_books.db").as_posix()

app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
db.init_app(app)

class Books(Base):
    __tablename__=r"books"
    id: Mapped[int] = mapped_column(primary_key= True)
    name: Mapped[str] = mapped_column(String(250),nullable= False, unique=True)
    author: Mapped[str] = mapped_column(String(250), nullable= False)
    rate: Mapped[float] = mapped_column(nullable=False)

with app.app_context():
    db.create_all()

all_books = []

@app.route('/')
def home():
    return render_template(
            'index.html',
            all_books= all_books,
        )


@app.route("/add", methods=["POST", "GET"])
def add():
    if request.method == "POST":
        book_record = {
            "book_name" : book_entry_form.get('book_name'),
            "book_author" : book_entry_form.get('book_author'),
            "book_rate" : book_entry_form.get('book_rate'),
        }
        all_books.append(book_record)

        book_obj = Books(name=book_record['book_name'], author=book_record['book_author'], rate= book_record['book_rate'])
        with app.app_context():
            db.session.add(book_obj)
            db.session.commit()

        return redirect(
                url_for('home', is_submited=True)
            )
    book_entry_form = BookEntry()
    return render_template('add.html', form= book_entry_form)

if __name__ == "__main__":
    app.run(debug=True)

