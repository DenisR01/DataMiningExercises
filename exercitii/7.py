# De pe 10 pagini de www.themoviedb.org ale unor filme, extrageti regizorul, durata si principalii actori.

import requests
from pyquery import PyQuery as pq
 
movie_array = [
    'https://www.themoviedb.org/movie/643586-willy-s-wonderland',
    'https://www.themoviedb.org/movie/471498-o2',
    'https://www.themoviedb.org/movie/14047-the-great-debaters',
    'https://www.themoviedb.org/movie/15184-a-good-woman',
    'https://www.themoviedb.org/movie/385128-fast-furious-9',
    'https://www.themoviedb.org/movie/460465-mortal-kombat',
    'https://www.themoviedb.org/tv/97180-selena-the-series',
    'https://www.themoviedb.org/tv/60735-the-flash',
    'https://www.themoviedb.org/movie/17035-the-amateurs',
    'https://www.themoviedb.org/movie/326947-the-maid'
]

headers = {
    'User-Agent': 'Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90',
}

for url in movie_array:
    response = requests.get(url, headers=headers)
    html = response.text
    dom = pq(html)
    director = pq(dom('.people .profile a')[0]).text()
    runtime = pq(dom('.runtime')[0]).text()
    actors = dom('.people.scroller .card p a')
    print(f'Regizor: {director}, Runtime: {runtime}, Actors:')
    for actor in actors:
        print(pq(actor).text())