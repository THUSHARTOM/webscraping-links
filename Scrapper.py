import requests
from bs4 import BeautifulSoup
import json
from urllib.parse import urlparse, urljoin
import string

sitename = "Cetera"                                     # Site to Scrape
# site URL
site_url = "https://advisor.foundingminds.in/index.html"
reqs = requests.get(site_url)
soup = BeautifulSoup(reqs.text, 'html.parser')
check = []


def remove(string):
    return string.strip()


def address_extraction():
    http_address = []
    menu = []
    for link in soup.find_all('a'):
        the_string = link.get('href')
        name = link.contents[0]
        try:
            name = remove(name)
            if name in ["", " "]:
                continue

            href = urljoin(site_url, the_string)
            http_address.append(href)
            menu.append(name)
            if name in menu:
                print(name)
        except:
            # print(name)
            continue

    # print(html_address, http_address)
    return http_address, menu


# Json data generation

def jsonbiulder(menuList, urls):
    data = {}
    data["site"] = {}
    data["site"]["sitename"] = sitename
    data["site"]["url"] = site_url
    data["site"]["haschild"] = "True"
    data["site"]["menus"] = []

    for i in range(len(urls)):
        data["site"]['menus'].append(
            str(menuList[i])
        )
        # print(urls[i])
        data["site"][menuList[i]] = {}
        data["site"][menuList[i]]["url"] = urls[i]
        data["site"][menuList[i]]["haschild"] = "False"
        data["site"][menuList[i]]["child"] = {}

    return data

# Json struct

# {
#     sitename(eg-"productHunt"):{
#         "menus":["login.html", "post", "discussions"],
#         "login.html":"https://www.producthunt.com/login",
#         "post":"https://www.producthunt.com/post",
#         "discussions":"https://www.producthunt.com/discussions/"
#     }
# }


if __name__ == "__main__":
    http_address, menu_list = address_extraction()
    # print(http_address)
    # print(len(http_address))
    # print(len(menu_list))
    json_data = jsonbiulder(menu_list, http_address)
    # print(json_data)
    filename = sitename + ".json"
    with open(filename, 'w') as json_file:
        json.dump(json_data, json_file)
