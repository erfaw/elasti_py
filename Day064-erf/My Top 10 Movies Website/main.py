from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length
import requests
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent
(ROOT_DIR / 'instance').mkdir(exist_ok=True)
db_path = (ROOT_DIR/"instance"/"movies.db").as_posix()

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{db_path}"
Bootstrap5(app)

class Base(DeclarativeBase): pass
db = SQLAlchemy(model_class=Base)
db.init_app(app)

class Movie(Base):
    __tablename__ = "Movies"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False,)
    year: Mapped[int] = mapped_column(nullable=False, )
    description: Mapped[str] = mapped_column(String(250) ,nullable=True)
    rating: Mapped[float] = mapped_column(nullable=False,)
    ranking: Mapped[int] = mapped_column(nullable=False,)
    review: Mapped[str] = mapped_column(String(1000) ,nullable=False,)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False,)
    def __repr__(self):
        return f"<Movie: id={self.id}, title={self.title}, year={self.year}, description={self.description}, rating={self.rating}, ranking={self.ranking}, review={self.review}, img_url={self.img_url}>"

with app.app_context():
    db.create_all()

class RateMovieForm(FlaskForm):
    rating = SelectField(label="Your Rating Out of 10", validators=[DataRequired()])
    review = StringField(label="Your Review", validators=[DataRequired(), Length(max= 70)])
    submit = SubmitField(label="Done")

@app.route("/")
def home():
    current_movies = db.session.execute(
        db.select(Movie).order_by(Movie.title)
    ).scalars().all()

    return render_template("index.html", movies= current_movies)

@app.route('/edit')
def edit():
    edit_form = RateMovieForm()
    edit_form.rating.choices = [_ for _ in range(10, -1, -1)]
    book_to_edit_id = request.args.get('id')
    book_to_edit = db.get_or_404(Movie, book_to_edit_id)
    return render_template(
        "edit.html",
        edit_form= edit_form,
        book_to_edit= book_to_edit,
    )

if __name__ == '__main__':
    app.run(debug=True)
