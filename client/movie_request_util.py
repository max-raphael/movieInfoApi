from typing import Optional

import requests

from service.models.movie_model import MovieModel


def main():
    title = get_title_from_user()
    movie: MovieModel = get_movie_from_service(title)
    if not movie:
        print("Sorry no movie found!")
        return

    print(f"{movie.title} was released in {movie.year} and directed by {movie.director}")


def get_title_from_user() -> str:
    return input("What title would you like to search for?")


def get_movie_from_service(title: str) -> Optional[MovieModel]:
    base_url = "http://127.0.0.1:8000/api/movie"
    response = requests.get(url=f"{base_url}/{title}")
    response.raise_for_status()

    return MovieModel(**response.json())


if __name__ == '__main__':
    main()
