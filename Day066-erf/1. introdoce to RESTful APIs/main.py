from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean, func
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent
(ROOT_DIR / "instance").mkdir(exist_ok= True)
db_path = ROOT_DIR / 'instance' / 'cafes.db'
db_path.as_posix()

app = Flask(__name__)

class Base(DeclarativeBase): pass

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

with app.app_context():
    db.create_all()
print()
@app.route("/")
def home():
    return render_template("index.html")

@app.route('/random')
def random():
    random_cafe = db.session.execute(
        db.select(Cafe).order_by(func.random()).limit(1)
    ).scalar_one_or_none()
    result: dict = {
        'id': random_cafe.id,
        'name': random_cafe.name,
        'img_url': random_cafe.img_url,
        'has_toilet': random_cafe.has_toilet,
        'has_sockets': random_cafe.has_sockets,
        'coffee_price': random_cafe.coffee_price,
        'map_url': random_cafe.map_url,
        'location': random_cafe.location,
        'seats': random_cafe.seats,
        'has_wifi': random_cafe.has_wifi,
        'can_take_calls': random_cafe.can_take_calls,
    }
    return result

# HTTP GET - Read Record

# HTTP POST - Create Record

# HTTP PUT/PATCH - Update Record

# HTTP DELETE - Delete Record

if __name__ == '__main__':
    app.run(debug=True)
