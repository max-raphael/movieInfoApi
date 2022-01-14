from pydantic import BaseModel
from typing import List


class MovieModel(BaseModel):
    title: str
    keywords: List[str] = []
    director: str
    year: int

    #
    # {
    #     "imdb_code": "tt0327850",
    #     "title": "The Rundown",
    #     "director": "Peter Berg",
    #     "keywords": [
    #         "amazon",
    #         "jungle",
    #         "hunter",
    #         "bounty hunter",
    #         "fight"
    #     ],
    #     "duration": 104,
    #     "genres": [
    #         "adventure",
    #         "action",
    #         "comedy",
    #         "thriller"
    #     ],
    #     "rating": "PG-13",
    #     "year": 2003,
    #     "imdb_score": 6.7
    # }
