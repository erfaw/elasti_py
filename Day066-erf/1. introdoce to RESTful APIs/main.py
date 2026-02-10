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
    def __repr__(self):
        return f"<Cafe: id={self.id}, name={self.name}>"
    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

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
    if random_cafe:
        return jsonify(random_cafe.to_dict())

@app.route('/all_cafes')
def all_cafes():
    all_cafes_records = db.session.execute(
        db.select(Cafe).order_by(Cafe.id)
    ).scalars().all()
    return jsonify(
            [cafe.to_dict() for cafe in all_cafes_records]
        )

if __name__ == '__main__':
    app.run(debug=True)
