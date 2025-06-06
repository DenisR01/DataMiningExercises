# De pe site-ul http://www.amazon.com/ , alegeti 10 produse din aceeasi categorie si extrageti:
# numele
# pretul
# descrierea
# cati oameni au gasi util al doilea comentariu afisat

import requests
from pyquery import PyQuery as pq

headers = {
    'dnt': '1',
    'downlink': '9.2',
    'ect': '4g',
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

products_array = [
    'https://www.amazon.com/EVGA-White-Warranty-Supply-100-W3-0600-K1/dp/B08WYHVCRP/ref=sr_1_1_sspa?dchild=1&qid=1621877523&s=computers-intl-ship&sr=1-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFLVTEwVDdKWENBQ0wmZW5jcnlwdGVkSWQ9QTEwMDk3MjIyWlo2TTFDM09ZUzQyJmVuY3J5cHRlZEFkSWQ9QTA1ODI2MDkyVElOT0VLNTE2TFM3JndpZGdldE5hbWU9c3BfYXRmX2Jyb3dzZSZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=',
    'https://www.amazon.com/2400Mbps-Bluetooth-Ultra-Low-802-11AX-Dual-Band/dp/B08ZQ1VFQR/ref=sr_1_2_sspa?dchild=1&qid=1621877523&s=computers-intl-ship&sr=1-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFLVTEwVDdKWENBQ0wmZW5jcnlwdGVkSWQ9QTEwMDk3MjIyWlo2TTFDM09ZUzQyJmVuY3J5cHRlZEFkSWQ9QTA2MzM4ODhHUklFTVlNNVczSVQmd2lkZ2V0TmFtZT1zcF9hdGZfYnJvd3NlJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==',
    'https://www.amazon.com/MLLIQUEA-Computer-Currency-Accessories-Included/dp/B094YHMWPP/ref=sr_1_3_sspa?dchild=1&qid=1621877523&s=computers-intl-ship&sr=1-3-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFLVTEwVDdKWENBQ0wmZW5jcnlwdGVkSWQ9QTEwMDk3MjIyWlo2TTFDM09ZUzQyJmVuY3J5cHRlZEFkSWQ9QTA0MTUwMjgzMzdGT1U4NUFIQVY5JndpZGdldE5hbWU9c3BfYXRmX2Jyb3dzZSZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=',
    'https://www.amazon.com/Seagate-Portable-External-Hard-Drive/dp/B07CRG94G3/ref=sr_1_4?dchild=1&qid=1621877523&s=computers-intl-ship&sr=1-4',
    'https://www.amazon.com/SAMSUNG-Inch-Internal-MZ-77E1T0B-AM/dp/B08QBJ2YMG/ref=sr_1_5?dchild=1&qid=1621877523&s=computers-intl-ship&sr=1-5',
    'https://www.amazon.com/Elements-Portable-External-Drive-WDBU6Y0050BBK-WESN/dp/B07X41PWTY/ref=sr_1_6?dchild=1&qid=1621877523&s=computers-intl-ship&sr=1-6',
    'https://www.amazon.com/Samsung-970-EVO-Plus-MZ-V7S1T0B/dp/B07MFZY2F2/ref=sr_1_7?dchild=1&qid=1621877523&s=computers-intl-ship&sr=1-7',
    'https://www.amazon.com/AMD-Ryzen-5950X-32-Thread-Processor/dp/B0815Y8J9N/ref=sr_1_8?dchild=1&qid=1621877523&s=computers-intl-ship&sr=1-8',
    'https://www.amazon.com/SanDisk-1TB-Extreme-Portable-SDSSDE61-1T00-G25/dp/B08GTYFC37/ref=sr_1_12?dchild=1&qid=1621877523&s=computers-intl-ship&sr=1-12',
    'https://www.amazon.com/EVGA-BRONZE-Warranty-Supply-100-BP-0510-K1/dp/B08N3X9WQQ/ref=sr_1_13_sspa?dchild=1&qid=1621877523&s=computers-intl-ship&sr=1-13-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFLVTEwVDdKWENBQ0wmZW5jcnlwdGVkSWQ9QTEwMDk3MjIyWlo2TTFDM09ZUzQyJmVuY3J5cHRlZEFkSWQ9QTA1ODI3MzMyMlpFR1M4MkUzTUVXJndpZGdldE5hbWU9c3BfbXRmX2Jyb3dzZSZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='
]

for url in products_array:
    response = requests.get(url, headers=headers)
    html = response.text
    dom = pq(html)
    product_name = pq(dom('#productTitle')[0]).text()
    product_price = pq(dom('#price_inside_buybox')[0]).text()
    product_description = pq(dom('#productDescription p')[0]).text()
    second_review_number = dom('.count')
    print(f'{product_name}, is priced at {product_price}, {product_description}, the second review was {second_review_number} times upvoted')