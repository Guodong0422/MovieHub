from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(100), nullable=False)
    director = db.Column(db.String(100))
    year = db.Column(db.Integer)
    genre = db.Column(db.String(50))
    rating = db.Column(db.Float)
    description = db.Column(db.Text)
    poster_url = db.Column(db.String(300))

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "director": self.director,
            "year": self.year,
            "genre": self.genre,
            "rating": self.rating,
            "description": self.description,
            "poster_url": self.poster_url
        }
class Watchlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    movie_id = db.Column(db.Integer, db.ForeignKey("movie.id"), nullable=False, unique=True)
    movie = db.relationship("Movie", backref=db.backref("watchlist_item", uselist=False))