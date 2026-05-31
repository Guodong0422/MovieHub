import csv
from app import app
from models import db, Movie


def import_movies_from_csv(file_path):
    with app.app_context():
        with open(file_path, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)

            count = 0
            skipped = 0

            for row in reader:
                title = row.get("title", "").strip()

                if not title:
                    skipped += 1
                    continue

                existing_movie = Movie.query.filter_by(title=title).first()

                if existing_movie:
                    skipped += 1
                    continue

                movie = Movie(
                    title=title,
                    director=row.get("director", "").strip(),
                    year=int(row["year"]) if row.get("year") else None,
                    genre=row.get("genre", "").strip(),
                    rating=float(row["rating"]) if row.get("rating") else None,
                    description=row.get("description", "").strip(),
                    poster_url=row.get("poster_url", "").strip()
                )

                db.session.add(movie)
                count += 1

            db.session.commit()

            print(f"Import completed.")
            print(f"Imported: {count} movies")
            print(f"Skipped: {skipped} rows")


if __name__ == "__main__":
    import_movies_from_csv("data/movies.csv")