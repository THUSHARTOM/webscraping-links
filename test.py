import requests
from bs4 import BeautifulSoup
import json

sitename = "Cetera"                                     # Site to Scrape
url = 'https://advisor.foundingminds.in/'                     # site URL
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')
check = []
def address_extraction():
    http_address = []
    # print(soup.find_all('a'))
    for link in soup.find_all():
        # the_string = link.get('href')
        print(str(link))
        break

address_extraction()