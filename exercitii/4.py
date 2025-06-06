# De pe pagina de amazon.com a unei cărți extrageți titlul cărții, autorul și anul de publicare.

import requests
from pyquery import PyQuery as pq

headers = {
    'dnt': '1',
    'downlink': '9.2',
    'ect': '4g',
    'referer': 'https://www.amazon.com/s?k=python+book&i=stripbooks-intl-ship&ref=nb_sb_noss_2',
    'rtt': '50',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
    'sec-ch-ua-mobile': '?0',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    'authority': 'www.amazon.com',
    'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
    'cookie': 'ubid-main=131-1392385-2252132; session-id-apay=140-3485257-1898004; session-id=147-9248670-5111113; session-id-time=2082787201l; i18n-prefs=USD; sp-cdn="L5Z9:RO"; session-token=UDVllsvcHpLV0sU5jeWDX3a9vo9K7CEYW2y8qNT8rv7UT9x20gMAuZ2/MmL1WBMfv5gUrXbpRZJk9IvnIhDc2I7Vhz/HLQ0NgC0d+7dH3PqWmzGa9c6VyHvqKri+WlT+N2bvhhd5FcA8i7v8gHTv32zWNmje5eTRIRCVSsbewjMT8xWHWr4/CfJht4Q5UzTa; skin=noskin; lc-main=en_US; csm-hit=tb:44M1779HHJD3QHMG6XW3+s-NZE5XGWBT7J9S980PYVD|1621876395287&t:1621876395287&adb:adblk_yes'
}

url = 'https://www.amazon.com/Python-Data-Analysis-Wrangling-IPython/dp/1491957662/ref=sr_1_6?dchild=1&keywords=python+book&qid=1621874947&s=books&sr=1-6'

response = requests.get(url, headers=headers)
html = response.text
dom = pq(html)
book_title = pq(dom('#productTitle')[0]).text()
book_author = pq(dom('span.author.notFaded span a')[2]).text()
book_publication_date = pq(dom('#detailBullets_feature_div ul li span.a-list-item span')[1]).text().split('(')[1].split(')')[0]

print(f'{book_title}, written by {book_author}, on {book_publication_date}')
