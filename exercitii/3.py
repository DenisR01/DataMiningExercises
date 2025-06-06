# De pe pagina de wikipedia a unei monede naționale extrageți utilizatorii monedei, simbolul, subdiviziunile și valoarea inflației

import requests
from pyquery import PyQuery as pq
 
url = 'https://en.wikipedia.org/wiki/Romanian_leu'
 
response = requests.get(url)
html = response.text
dom = pq(html)
row_head_elements = dom('.infobox tr th[scope=row]')
currency_user = pq(dom('.infobox tr th[scope=row]+td span.flagicon+a')[0]).text()
currency_symbol = pq(dom('.infobox tr th[scope=row]+td')[0]).text()
currency_subdivision = pq(dom('.infobox tr th[scope=row] span.nobold')[0]).text()
currnecy_inflation = pq(dom('.infobox tr th[scope=row]+td')[21]).text().split('[')[0]


print(f'Currency user: {currency_user}, Currency Simbol {currency_symbol}, Currency Subdivision {currency_subdivision}, Inflation {currnecy_inflation}')