from pathlib import Path
import json
import logging

# Set path of the database
DB = Path(__file__).resolve().parent / 'data/movies.json'


def get_movies():
    """List movie(s) from the database"""
    if DB.stat().st_size == 0:
        return []

    with open(DB, 'r') as f:
        movies_title = json.load(f)

    movies = [Movie(movie_title) for movie_title in movies_title]
    return movies


def _write_movies(movies):
    """Write movie(s) to the database"""
    with open(DB, 'w') as f:
        json.dump(sorted(movies), f, indent=4)


def _get_movies():
    """Read movie(s) from the database"""
    if DB.stat().st_size == 0:
        return []

    with open(DB, 'r') as f:
        return json.load(f)


class Movie:

    def __init__(self, title: str):
        self.title = title.title()

    def __str__(self):
        return self.title

    def add_to_movies(self):
        """Add a new movie in the database"""
        movies = _get_movies()

        if self.title not in movies:
            movies.append(self.title)
            _write_movies(movies)
            return True
        else:
            logging.warning(
                f'''Le film '{self.title}' est déjà présent dans la base de données.
            ''')
            return False

    def remove_from_movies(self):
        """Remove a movie from the database"""
        movies = _get_movies()

        if self.title in movies:
            movies.remove(self.title)
            _write_movies(movies)


if __name__ == '__main__':
    pass
