### Sample pages
# https://sitename/login/topic/page1.html
# https://sitename/posts/topic/page1
# https://sitename/posts/page2
# https://sitename/posts/topic/subtopic/page3
# https://sitename/discussions/topic/page1

### JSON format

## Method 1

# data = {
#     "sitename":
#         {
#             "menus": ["login#page1", "post#page1", "post#page2", "post#page3","discussion#page1"],
#             "login#page1": "page1_address",
#             "post#page1": "page1_address",
#             "post#page2": "page2_address",
#             "post#page3": "page3_address",
#             "discussion#page1": "page1_address"
#         }
# }

## Method 2

# data = {
#     "sitename":
#         {
#             "menus": ["login", "post#page1", "post#page2", "post#page3","discussion#page1"],
#             "login": ["page1": "page1_address"],
#             "post": ["page1": "page1_address","page2": "page2_address", "page3": "page3_address"],
#             "discussion": ["page1": "page1_address"]
#         }
#
# }