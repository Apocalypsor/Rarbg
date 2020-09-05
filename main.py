# -*- coding: utf-8 -*-

from typing import Optional

import uvicorn
from fastapi import FastAPI, Query, Path, Response

from rarbg.searchRarbg import getResult

tags_metadata = [
    {
        "name": "Search",
        "externalDocs": {
            "description": "Avaliable Categories",
            "url": "https://github.com/Apocalypsor/Rarbg/tree/master/rarbg/Categories.md",
        },
    },
    {
        "name": "Latest"
    }
]

app = FastAPI(
    title='Customed RARBG feed',
    openapi_tags=tags_metadata
)

@app.get('/search/{title}', summary='Search by title.', tags=["Search"])
def generateSearch(
    title: str = Path(..., description='Title'),
    category: Optional[set] = Query(None, description='Category')
):
    status, output = getResult('title', title, category)

    if status:
        return Response(content=output, media_type='application/rss+xml')

    return Response(content=f'Error: {output}')

@app.get('/imdb/{imdb}', summary='Search by IMDb index.', tags=["Search"])
def generateIMDb(
    imdb: str = Path(..., description='IMDb ID'),
    category: Optional[set] = Query(None, description='Category')
):
    status, output = getResult('imdb', imdb, category)

    if status:
        return Response(content=output, media_type='application/rss+xml')

    return Response(content=f'Error: {output}')

@app.get('/tvdb/{tvdb}', summary='Search by TheTVDB index.', tags=["Search"])
def generateTVDb(
    tvdb: str = Path(..., description='TheTVDB ID'),
    category: Optional[set] = Query(None, description='Category')
):
    status, output = getResult('tvdb', tvdb, category)

    if status:
        return Response(content=output, media_type='application/rss+xml')

    return Response(content=f'Error: {output}')

@app.get('/tmdb/{tmdb}', summary='Search by TMDb index.', tags=["Search"])
def generateTMDb(
    tmdb: str = Path(..., description='TMDb ID'),
    category: Optional[set] = Query(None, description='Category')
):
    status, output = getResult('tmdb', tmdb, category)

    if status:
        return Response(content=output, media_type='application/rss+xml')

    return Response(content=f'Error: {output}')

@app.get('/latest', summary='List latest torrents.', tags=["Latest"])
def generateLatest():
    status, output = getResult('latest')

    if status:
        return Response(content=output, media_type='application/rss+xml')

    return Response(content=f'Error: {output}')

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000, debug=True)
