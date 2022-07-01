import json

"========= JSON ========="
# JSON - Java Script Object Notation - one of the most popular types of data that most languages understand
# with open('test.json', 'w') as file:
#     # Record in JSON
#     dict_ = {
#         'products': [
#             {
#                 'id': 1,
#                 'name': 'snickers',
#                 'price': 45,
#             },
#             {
#                 'id': 2,
#                 'name': 'bounty',
#                 'price': 45,
#             }
#         ]
#     }
#     # dump - writes a dictionary into the file in JSON format
#     json.dump(dict_, file)


# with open('test.json', 'r') as file:
    # Reading from JSON
    # dict_ = json.load(file)
    # print(dict_)


# dict ==DUMP==> JSON file
# file ==LOAD==> dict


# The work with modules is like working with packages but you need to indicate the path
from product.models import create_product

create_product(1, 20, 'chips')