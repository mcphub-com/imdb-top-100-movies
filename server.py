import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/rapihub-rapihub-default/api/imdb-top-100-movies'

mcp = FastMCP('imdb-top-100-movies')

@mcp.tool()
def top100_movies_list() -> dict: 
    '''The cover image, rank, title, thumbnail, IMDb rating, ID, year, description, imdb id, imdb link and genre of the top 100 movies of all time. More detailed information about the movies and their trailers can be accessed through the 'Movie Data By ID' endpoint. Regular updates.'''
    url = 'https://imdb-top-100-movies.p.rapidapi.com/'
    headers = {'x-rapidapi-host': 'imdb-top-100-movies.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def movie_data_by_id(id: Annotated[str, Field(description='')]) -> dict: 
    '''This endpoint lists a movie's data by its ID. It contains a big-sized cover image, trailer, description, and more. For example, you can use the ID 'top32'.'''
    url = 'https://imdb-top-100-movies.p.rapidapi.com/top32'
    headers = {'x-rapidapi-host': 'imdb-top-100-movies.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def top100_series_list() -> dict: 
    '''The cover image, rank, title, thumbnail, IMDb rating, ID, year, description, imdb id, imdb link and genre of the top 100 series of all time. More detailed information about the series and their trailers can be accessed through the 'Series Data By ID' endpoint. Regular updates.'''
    url = 'https://imdb-top-100-movies.p.rapidapi.com/series/'
    headers = {'x-rapidapi-host': 'imdb-top-100-movies.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def series_data_by_id(id: Annotated[str, Field(description='')]) -> dict: 
    '''This endpoint lists a series's data by its ID. It contains a large-sized cover image, trailer, description, and more. For example, you can use the ID 'top1'.'''
    url = 'https://imdb-top-100-movies.p.rapidapi.com/series/top1'
    headers = {'x-rapidapi-host': 'imdb-top-100-movies.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
