# De pe site-ul http://www.crunchbase.com/ , pentru o companie oarecare, extrageti locatia companiei, numărul de angajați, website-ul și totalul fondurilor primite.

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
    'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
    'cookie': 'ubid-main=131-1392385-2252132; session-id-apay=140-3485257-1898004; session-id=147-9248670-5111113; session-id-time=2082787201l; i18n-prefs=USD; sp-cdn="L5Z9:RO"; session-token=UDVllsvcHpLV0sU5jeWDX3a9vo9K7CEYW2y8qNT8rv7UT9x20gMAuZ2/MmL1WBMfv5gUrXbpRZJk9IvnIhDc2I7Vhz/HLQ0NgC0d+7dH3PqWmzGa9c6VyHvqKri+WlT+N2bvhhd5FcA8i7v8gHTv32zWNmje5eTRIRCVSsbewjMT8xWHWr4/CfJht4Q5UzTa; skin=noskin; lc-main=en_US; csm-hit=tb:44M1779HHJD3QHMG6XW3+s-NZE5XGWBT7J9S980PYVD|1621876395287&t:1621876395287&adb:adblk_yes'
}

url = 'https://www.crunchbase.com/organization/ibm'

response = requests.get(url, headers=headers)
html = response.text
dom = pq(html)
location = pq(dom('body > chrome > div > mat-sidenav-container > mat-sidenav-content > div > ng-component > entity-v2 > page-layout > div > div > div > page-centered-layout.overview-divider.ng-star-inserted > div > row-card > div > div:nth-child(1) > profile-section > section-card > mat-card > div.section-content-wrapper > div > fields-card > ul > li:nth-child(1) > label-with-icon > span > field-formatter > identifier-multi-formatter > span > a:nth-child(2)')[0]).text()
employee_no = pq(dom('mat-sidenav-container > mat-sidenav-content > div > ng-component > entity-v2 > page-layout > div > div > div > page-centered-layout.overview-divider.ng-star-inserted > div > row-card > div > div:nth-child(1) > profile-section > section-card > mat-card > div.section-content-wrapper > div > fields-card > ul > li:nth-child(2) > label-with-icon > span > field-formatter > a')[0]).text()
website = pq(dom('mat-sidenav-container > mat-sidenav-content > div > ng-component > entity-v2 > page-layout > div > div > div > page-centered-layout.overview-divider.ng-star-inserted > div > row-card > div > div:nth-child(1) > profile-section > section-card > mat-card > div.section-content-wrapper > div > fields-card > ul > li:nth-child(4) > label-with-icon > span > field-formatter > link-formatter > a')[0]).text()
investments_no = pq(dom('mat-sidenav-container > mat-sidenav-content > div > ng-component > entity-v2 > page-layout > div > div > div > page-centered-layout.overview-divider.ng-star-inserted > div > row-card > div > div:nth-child(2) > profile-section > section-card > mat-card > div.section-content-wrapper > div > anchored-values > div:nth-child(2) > a > div > field-formatter > span')[0]).text()

print(f'IBM HQ is in {location}, with a no# of employees of {employee_no}, {website} is the website adress, and the number of investors fundings are {investments_no}.')


