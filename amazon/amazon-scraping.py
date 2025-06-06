from bs4 import BeautifulSoup as bs
import requests

headers = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})

urls = ['https://www.amazon.com/Rise-America-Remaking-World-Order/dp/154452143X/ref=zg_bsnr_books_73?_encoding=UTF8&psc=1&refRID=EPG8JM4TYA0BA8P1JQBY',
        'https://www.amazon.com/Brat-80s-Story-Andrew-McCarthy/dp/1538754274/ref=zg_bsnr_books_74?_encoding=UTF8&psc=1&refRID=EPG8JM4TYA0BA8P1JQBY',
        'https://www.amazon.com/Silent-Patient-Alex-Michaelides/dp/125030170X/ref=zg_bsnr_books_75?_encoding=UTF8&psc=1&refRID=EPG8JM4TYA0BA8P1JQBY',
        'https://www.amazon.com/Unsettled-Climate-Science-Doesnt-Matters/dp/1950665798/ref=zg_bsnr_books_76?_encoding=UTF8&psc=1&refRID=EPG8JM4TYA0BA8P1JQBY',
        'https://www.amazon.com/Helgoland-Making-Sense-Quantum-Revolution/dp/0593328884/ref=zg_bsnr_books_77?_encoding=UTF8&psc=1&refRID=EPG8JM4TYA0BA8P1JQBY',
        'https://www.amazon.com/Tell-Bees-That-Gone-Outlander/dp/1101885688/ref=zg_bsnr_books_78?_encoding=UTF8&psc=1&refRID=EPG8JM4TYA0BA8P1JQBY',
        'https://www.amazon.com/Great-Circle-novel-Maggie-Shipstead/dp/0525656979/ref=zg_bsnr_books_79?_encoding=UTF8&psc=1&refRID=EPG8JM4TYA0BA8P1JQBY',
        'https://www.amazon.com/Juneteenth-Annette-Gordon-Reed/dp/1631498835/ref=zg_bsnr_books_80?_encoding=UTF8&psc=1&refRID=EPG8JM4TYA0BA8P1JQBY',
        'https://www.amazon.com/Newcomer-Novel-Mary-Kay-Andrews/dp/1250256968/ref=zg_bsnr_books_81?_encoding=UTF8&psc=1&refRID=EPG8JM4TYA0BA8P1JQBY',
        'https://www.amazon.com/Stamped-Kids-Racism-Antiracism-You/dp/0316167584/ref=zg_bsnr_books_82?_encoding=UTF8&psc=1&refRID=EPG8JM4TYA0BA8P1JQBY'
]

for url in urls:
    page = requests.get(url, headers=headers)
    soup = bs(page.text, 'html.parser')
    title = soup.find('span', {'id':'productTitle'}).text
    author = soup.find('a', {'class': 'a-link-normal contributorNameID'}).text
    subtitle = soup.find('span', {'id': 'productSubtitle'}).text
    year = subtitle[-5:]

    print(f'\nTitlul cartii: {title}Autorul: {author} \nAnul de publicare: {year}\n-------------------------------')
