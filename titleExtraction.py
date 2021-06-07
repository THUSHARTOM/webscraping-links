import requests
import bs4 

req = requests.get("https://advisor.foundingminds.in/")

# print(req.text)
soup = bs4.BeautifulSoup(req.text, 'html.parser')
title = soup.select('title')
print(title[0].getText())