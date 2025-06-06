# De pe pagina de metacritic a unui film, extrageti regizorul, scorul mediu acordat de critici, scorul mediu acordat de utilizatori și durata filmului.

import requests
from pyquery import PyQuery as pq

headers = {
    'User-Agent': 'Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90',
}

url = 'https://www.metacritic.com/movie/mortal-kombat-2021'

response = requests.get(url, headers=headers)
html = response.text
dom = pq(html)
movie_director = pq(dom('.details_section .director a span')[0]).text()
movie_runtime = pq(dom('.details_section .runtime span')[1]).text()
movie_critics_rating = pq(dom('.metascore_anchor span')[0]).text()
movie_users_rating = pq(dom('.metascore_anchor span')[1]).text()

print(f'Movie Director: {movie_director}, Movie Runtime: {movie_runtime}, Average critics rating: {movie_critics_rating}, Average users rating: {movie_users_rating}')
