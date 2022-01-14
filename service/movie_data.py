from typing import Optional

import httpx

from models.movie_model import MovieModel

BASE_URL = "https://movieservice.talkpython.fm/api"
SEARCH = "search"


async def get_movie(title_subtext) -> Optional[MovieModel]:
    url = f"{BASE_URL}/{SEARCH}/{title_subtext}"
    async with httpx.AsyncClient() as client:
        resp: httpx.Response = await client.get(url)
        print(resp, resp.text)
        resp.raise_for_status()
        data = resp.json()

    results = data['hits']
    if not results:
        return None

    # the ** notation returns dict key values as keyword arguments in the function call
    movie = MovieModel(**results[0])

    return movie
