from flask import Flask, render_template, request, redirect, url_for, jsonify
from models import db, Movie, Watchlist
from sqlalchemy import func

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)


@app.route("/")
def index():
    search = request.args.get("search", "")
    genre = request.args.get("genre", "")
    sort = request.args.get("sort", "rating_desc")

    query = Movie.query

    # Search by movie title
    if search:
        query = query.filter(Movie.title.contains(search))

    # Filter by genre
    if genre:
        query = query.filter(Movie.genre == genre)

    # Sort results
    if sort == "rating_desc":
        query = query.order_by(Movie.rating.desc())
    elif sort == "rating_asc":
        query = query.order_by(Movie.rating.asc())
    elif sort == "year_desc":
        query = query.order_by(Movie.year.desc())
    elif sort == "year_asc":
        query = query.order_by(Movie.year.asc())
    else:
        query = query.order_by(Movie.id.desc())

    movies = query.all()

    genres = [
        "Action",
        "Drama",
        "Comedy",
        "Sci-Fi",
        "Animation",
        "Horror",
        "Romance",
        "Thriller"
    ]

    return render_template(
        "index.html",
        movies=movies,
        search=search,
        genre=genre,
        sort=sort,
        genres=genres
    )


@app.route("/movie/<int:movie_id>")
def movie_detail(movie_id):
    movie = Movie.query.get_or_404(movie_id)

    similar_movies = (
        Movie.query
        .filter(Movie.genre == movie.genre)
        .filter(Movie.id != movie.id)
        .order_by(Movie.rating.desc())
        .limit(3)
        .all()
    )

    return render_template(
        "detail.html",
        movie=movie,
        similar_movies=similar_movies
    )

@app.route("/add", methods=["GET", "POST"])
def add_movie():
    if request.method == "POST":
        title = request.form.get("title")
        director = request.form.get("director")
        year = request.form.get("year")
        genre = request.form.get("genre")
        rating = request.form.get("rating")
        description = request.form.get("description")
        poster_url = request.form.get("poster_url")

        new_movie = Movie(
            title=title,
            director=director,
            year=year,
            genre=genre,
            rating=rating,
            description=description,
            poster_url=poster_url
        )

        db.session.add(new_movie)
        db.session.commit()

        return redirect(url_for("index"))

    return render_template("add_movie.html")


@app.route("/edit/<int:movie_id>", methods=["GET", "POST"])
def edit_movie(movie_id):
    movie = Movie.query.get_or_404(movie_id)

    if request.method == "POST":
        movie.title = request.form.get("title")
        movie.director = request.form.get("director")
        movie.year = request.form.get("year")
        movie.genre = request.form.get("genre")
        movie.rating = request.form.get("rating")
        movie.description = request.form.get("description")
        movie.poster_url = request.form.get("poster_url")

        db.session.commit()

        return redirect(url_for("movie_detail", movie_id=movie.id))

    return render_template("edit_movie.html", movie=movie)


@app.route("/delete/<int:movie_id>", methods=["POST"])
def delete_movie(movie_id):
    movie = Movie.query.get_or_404(movie_id)

    db.session.delete(movie)
    db.session.commit()

    return redirect(url_for("index"))

@app.route("/watchlist")
def watchlist():
    watchlist_items = Watchlist.query.all()
    return render_template("watchlist.html", watchlist_items=watchlist_items)


@app.route("/watchlist/add/<int:movie_id>", methods=["POST"])
def add_to_watchlist(movie_id):
    movie = Movie.query.get_or_404(movie_id)

    existing_item = Watchlist.query.filter_by(movie_id=movie.id).first()

    if not existing_item:
        new_item = Watchlist(movie_id=movie.id)
        db.session.add(new_item)
        db.session.commit()

    return redirect(url_for("movie_detail", movie_id=movie.id))


@app.route("/watchlist/remove/<int:movie_id>", methods=["POST"])
def remove_from_watchlist(movie_id):
    item = Watchlist.query.filter_by(movie_id=movie_id).first_or_404()

    db.session.delete(item)
    db.session.commit()

    return redirect(url_for("watchlist"))

@app.route("/api/movies")
def api_movies():
    movies = Movie.query.all()
    return jsonify([movie.to_dict() for movie in movies])


@app.route("/api/movies/<int:movie_id>")
def api_movie_detail(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    return jsonify(movie.to_dict())

@app.route("/dashboard")
def dashboard():
    total_movies = Movie.query.count()

    average_rating = db.session.query(func.avg(Movie.rating)).scalar()
    if average_rating:
        average_rating = round(average_rating, 2)
    else:
        average_rating = 0

    top_movie = Movie.query.order_by(Movie.rating.desc()).first()

    genre_counts = (
        db.session.query(Movie.genre, func.count(Movie.id))
        .group_by(Movie.genre)
        .order_by(func.count(Movie.id).desc())
        .all()
    )

    most_common_genre = genre_counts[0][0] if genre_counts else "N/A"

    return render_template(
        "dashboard.html",
        total_movies=total_movies,
        average_rating=average_rating,
        top_movie=top_movie,
        genre_counts=genre_counts,
        most_common_genre=most_common_genre
    )

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)