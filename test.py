import requests
from bs4 import BeautifulSoup
import json
from urllib.parse import urlparse, urljoin
import string


sitename = "Cetera"                                     # Site to Scrape
url = 'https://advisor.foundingminds.in/'                     # site URL
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'lxml')

href_list = []
menu_list = []
data = {}


def remove(string):
    return string.translate(None, ' \n\t\r')


for a_tag in soup.findAll("a"):
    name = a_tag.contents[0]
    href = a_tag.attrs.get("href")
    if href == "" or href is None or href == "#":
        # href empty tag
        continue
    if name not in menu_list:
        result = name.find('<')  # Clearing out junk name. Modify this
        if result:
            # print(name)
            # print("\n")
            # # name = remove(name)
            # menu_list.append(name)

            href = urljoin(url, href)
            print(href)
            print("\n")
            # href_list.append(href)

            # data[name] = href
        else:
            # pass
            print(name)

    # print("\n")

# print(href_list)
# print(menu_list)
# print(data)
