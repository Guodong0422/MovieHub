# MovieHub: Movie Content Management and Discovery Platform
[English README](README.md) | [产品需求文档](docs/PRD_CN.md) | [英文 PRD](docs/PRD.md) | [许可证](LICENSE) | [中文许可证说明](LICENSE_CN.md)

MovieHub is a Flask-based movie content management and discovery platform.

It supports movie CRUD operations, CSV dataset import, search and filtering, REST API access, dashboard analytics, watchlist management, and rule-based similar movie recommendations.

This project was rebuilt and extended as a portfolio project to demonstrate full-stack development, database design, API design, data management, and product thinking.

---

## Product Background

Many movie catalogue systems require users or content managers to manage large amounts of movie metadata, including movie titles, genres, ratings, release years, descriptions, and posters.

MovieHub is designed as a lightweight content management and discovery platform that allows users to:

* Manage movie information
* Import movie datasets from CSV files
* Search, filter, and sort movie records
* View content analytics through a dashboard
* Save movies to a personal watchlist
* Discover similar movies based on genre and rating

The project simulates the core workflow of a small-scale content platform or media catalogue management system.

---

## Core Features

### Movie Management

* Add new movie records
* View all movies on the homepage
* View detailed movie information
* Edit existing movie records
* Delete movie records

### Search, Filter, and Sort

* Search movies by title
* Filter movies by genre
* Sort movies by rating
* Sort movies by release year

### CSV Dataset Import

* Import movie data from a CSV file
* Map CSV fields to database columns
* Convert year and rating fields into appropriate data types
* Skip duplicate movie records based on title

### REST API

* `GET /api/movies`
  Return all movie records in JSON format.

* `GET /api/movies/<id>`
  Return a single movie record by ID.

### Dashboard Analytics

The dashboard provides basic product and data insights, including:

* Total number of movies
* Average movie rating
* Top-rated movie
* Most common genre
* Genre distribution

### Watchlist

* Add movies to a personal watchlist
* View saved movies on a dedicated watchlist page
* Remove movies from the watchlist

### Similar Movie Recommendation

* Recommend movies with the same genre
* Exclude the current movie from recommendations
* Rank recommended movies by rating
* Display up to three similar movies on the movie detail page

---

## Tech Stack

* Python
* Flask
* Flask-SQLAlchemy
* SQLite
* HTML
* CSS
* Bootstrap
* REST API
* CSV data import
* Git / GitHub

---

## Project Structure

```text
moviehub/
├── app.py
├── models.py
├── import_movies.py
├── requirements.txt
├── README.md
├── data/
│   └── movies.csv
├── static/
│   └── style.css
└── templates/
    ├── add_movie.html
    ├── base.html
    ├── dashboard.html
    ├── detail.html
    ├── edit_movie.html
    ├── index.html
    └── watchlist.html
```

---

## How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/Guodong0422/MovieHub.git
cd moviehub
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

On Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

If activation is not available, the project can also be run directly with:

```powershell
.\venv\Scripts\python.exe app.py
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Flask application

```bash
python app.py
```

Then open:

```text
http://127.0.0.1:5000
```

---

## Import Movie Dataset

Movie data can be imported from:

```text
data/movies.csv
```

Run:

```bash
python import_movies.py
```

The import script reads the CSV file, checks for duplicate movie titles, converts fields such as year and rating, and inserts new movie records into the SQLite database.

---

## API Endpoints

### Get all movies

```http
GET /api/movies
```

Example response:

```json
[
  {
    "id": 1,
    "title": "Inception",
    "director": "Christopher Nolan",
    "year": 2010,
    "genre": "Sci-Fi",
    "rating": 8.8,
    "description": "A thief enters people's dreams to steal and plant ideas.",
    "poster_url": "https://example.com/poster.jpg"
  }
]
```

### Get movie by ID

```http
GET /api/movies/1
```

Example response:

```json
{
  "id": 1,
  "title": "Inception",
  "director": "Christopher Nolan",
  "year": 2010,
  "genre": "Sci-Fi",
  "rating": 8.8,
  "description": "A thief enters people's dreams to steal and plant ideas.",
  "poster_url": "https://example.com/poster.jpg"
}
```

---

## Product Thinking

MovieHub was designed not only as a technical CRUD application, but also as a small product prototype.

The project includes several product-oriented design considerations:

* Search and filtering improve content discovery efficiency.
* CSV import supports content operation and data initialization workflows.
* Dashboard metrics help content managers understand catalogue structure.
* Watchlist captures basic user preference signals.
* Similar movie recommendations simulate a basic content discovery scenario.
* REST API design supports future frontend or external client integration.

---

## User Stories

### User Story 1: Search and Discovery

As a movie viewer, I want to search and filter movies so that I can quickly find content I am interested in.

### User Story 2: Content Management

As a content manager, I want to add, edit, and delete movie records so that the movie catalogue can be maintained efficiently.

### User Story 3: Dataset Import

As a content operator, I want to import movie data from a CSV file so that I do not need to manually create each movie record.

### User Story 4: Product Analytics

As a product manager, I want to view dashboard metrics so that I can understand the structure and quality of the movie catalogue.

### User Story 5: Watchlist

As a user, I want to save movies to a watchlist so that I can easily revisit movies I am interested in.

### User Story 6: Recommendation

As a user, I want to see similar movies on a movie detail page so that I can discover more relevant content.

---

## Current Limitations

This project is currently a local Flask application and does not include:

* User authentication
* Multi-user account management
* Cloud database deployment
* Production-level security configuration
* Advanced machine learning recommendation models

These limitations are intentionally kept to maintain the project as a lightweight portfolio prototype.

---

## Future Improvements

Potential future improvements include:

* User login and authentication
* Personalized recommendations based on watchlist and rating behavior
* User reviews and rating system
* Web-based CSV upload interface
* API documentation page
* Pagination for larger datasets
* Deployment on Render, Railway, or PythonAnywhere
* Static project showcase page using GitHub Pages

---

## Portfolio Summary

This project demonstrates:

* Full-stack web development with Flask
* Relational database design with SQLite and SQLAlchemy
* REST API design and JSON data response
* CSV data processing and batch import
* Search, filtering, and sorting logic
* Dashboard analytics and product metrics
* User behavior feature design through Watchlist
* Rule-based recommendation logic
* Product thinking and feature planning
