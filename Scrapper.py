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
    for link in soup.find_all('a'):
        the_string = link.get('href')
        # print(the_string)
        check.append(the_string)

        if str(the_string).startswith("http"):
            http_address.append(the_string)
        if str(the_string).startswith("/"):
            part1 = the_string.split("/",1)[1]
            if str(url + part1) not in http_address:
                # if "?" not in part1 and "#" not in part1 :
                http_address.append(url + part1)
        if str(the_string).endswith(".html"):
            if str(url + the_string) not in http_address:
                http_address.append(url + the_string)
        # else:
        #     for part in the_string.split("/"):
        #         print(part[0])
                # topics.append(part[1])

    # print(html_address, http_address)
    # print(topics)
    return http_address


### Generating menu list
def menuListGeneration(address):
    menu_list = []
    http_address = []
    for item in address:
        try:
            check = item.split("/")[-1]
            if check not in " ":
                # print(check)
                # print(item)
                menu_list.append(check)
                http_address.append(item)
            else:
                check = item.split("/")[-2]
                menu_list.append(check)
                http_address.append(item)
                # print(check)
                # print(item)
        except Exception as e:
            print("This item caused an exception", item)
    return menu_list, http_address



### Json data generation

def jsonbiulder(menuList, urls):
    data = {}
    data[sitename] = {}
    data[sitename]['menus'] = []

    for i in range(len(urls)):
        data[sitename]['menus'].append(
            str(menuList[i])
        )
        data[sitename][menuList[i]] = urls[i]

    return data

### Json struct

# {
#     sitename(eg-"productHunt"):{
#         "menus":["login.html", "post", "discussions"],
#         "login.html":"https://www.producthunt.com/login",
#         "post":"https://www.producthunt.com/post",
#         "discussions":"https://www.producthunt.com/discussions/"
#     }
# }


if __name__ == "__main__":
    http_address = address_extraction()
    # print(http_address)
    menu_list, http_address = menuListGeneration(http_address)
    print(len(http_address))
    print(len(menu_list))
    json_data = jsonbiulder(menu_list, http_address)
    print(json_data)
    with open('test.json', 'w') as json_file:
        json.dump(json_data, json_file)