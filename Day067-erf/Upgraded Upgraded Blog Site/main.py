from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date
from pathlib import Path
import os
from dotenv import load_dotenv

ROOT_DIR = Path(__file__).resolve().parent
(ROOT_DIR / "instance").mkdir(exist_ok= True)
db_path = ROOT_DIR / 'instance' / 'posts.db'
db_path.as_posix()

load_dotenv(ROOT_DIR/'.env')

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
class Base(DeclarativeBase): pass
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
db = SQLAlchemy(model_class=Base)
db.init_app(app)
app.config['CKEDITOR_PKG_TYPE'] = 'full'
ckeditor = CKEditor(app)

class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)
    def __repr__(self):
        return f"<BlogPost: id={self.id}, title={self.title}>"
    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

with app.app_context():
    db.create_all()

@app.route('/')
def get_all_posts():
    posts = db.session.execute(
        db.select(BlogPost).order_by(BlogPost.date.desc())
    ).scalars().all()
    return render_template("index.html", all_posts=posts)

@app.route('/posts/<int:post_id>')
def show_post(post_id):
    requested_post = db.get_or_404(BlogPost, post_id)
    return render_template("post.html", post=requested_post)

class MakePostForm(FlaskForm):
    title= StringField(label="Title", validators=[DataRequired()])
    subtitle= StringField(label="Subtitle", validators=[DataRequired()])
    author= StringField(label="Author", validators=[DataRequired()])
    img_url= StringField(label="Image URL", validators=[DataRequired(), URL()])
    body= CKEditorField(label="Main Content", validators=[DataRequired()])
    submit= SubmitField(label="Submit")

@app.route('/new-post', methods=["POST", "GET"])
def add_new_post():
    form= MakePostForm()
    return render_template(
        'make-post.html',
        form= form,
    )

# TODO: edit_post() to change an existing blog post

# TODO: delete_post() to remove a blog post from the database

# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True, port=5003)
