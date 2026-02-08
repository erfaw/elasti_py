from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired, Length, NumberRange
import requests
from pathlib import Path
from dotenv import load_dotenv
import os
ROOT_DIR = Path(__file__).resolve().parent
load_dotenv(ROOT_DIR/'.env')
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
    rating = FloatField(label="Your Rating Out of 10 .e.g 6.8", validators=[DataRequired(), NumberRange(min=0.0, max=10.0)])
    review = StringField(label="Your Review", validators=[DataRequired(), Length(max= 25)])
    submit = SubmitField(label="Done")
class AddMovieForm(FlaskForm):
    title = StringField(label="Movie Title", validators=[DataRequired()])
    submit = SubmitField(label="Add Movie")

def get_movie_data(movie_title:str) -> list[dict]:
    """
    makes a get request to
    
        "http://www.omdbapi.com"
    
    in order to get data about a specific movie name

    **NOTICE** : not work with normal network in Iran!
    
    :param movie_title:
    :type movie_title: str
    :return: Request response with dict(json) format
    :rtype: dict
    """
    api_url = "http://www.omdbapi.com"
    params = {
        "apikey": os.environ.get('omdb_api_key'),
        "s": movie_title,
        "type": "movie",
    }
    result = requests.get(
        url= api_url,
        params= params,
    ).json()['Search']
    return result


@app.route("/")
def home():
    current_movies = db.session.execute(
        db.select(Movie).order_by(Movie.title)
    ).scalars().all()

    return render_template("index.html", movies= current_movies)

@app.route('/edit', methods=["POST", "GET"])
def edit():
    edit_form = RateMovieForm()
    movie_to_edit_id = request.args.get('id')
    movie_to_edit = db.get_or_404(Movie, movie_to_edit_id)
    if edit_form.validate_on_submit():
        movie_to_edit.rating = edit_form.rating.data
        movie_to_edit.review = edit_form.review.data
        db.session.commit()
        return redirect(
            url_for('home', is_updated=True)
        )
    return render_template(
        "edit.html",
        form= edit_form,
        movie= movie_to_edit,
    )

@app.route('/delete')
def delete():
    movie_to_delete_id = request.args.get('id')
    movie_to_delete = db.get_or_404(Movie, movie_to_delete_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(
        url_for('home', is_removed=True)
    )

@app.route('/add', methods=["POST", "GET"])
def add():
    add_movie_form = AddMovieForm()
    if add_movie_form.validate_on_submit():
        add_movie_name_str = add_movie_form.title.data
        movie_responses:list = get_movie_data(add_movie_name_str)
        return render_template(
                'select.html',
                movies= movie_responses,
            )
    return render_template(
        'add.html',
        form= add_movie_form,
    )

if __name__ == '__main__':
    app.run(debug=True)
