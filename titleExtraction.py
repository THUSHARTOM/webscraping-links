import requests
import bs4

req = requests.get("https://dev.otw.redtailtechnology.com/dashboard/overview")

# print(req.text)
soup = bs4.BeautifulSoup(req.text, 'html.parser')
title = soup.select('title')
print(title[0].getText())
