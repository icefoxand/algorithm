import json
from pprint import pprint


def book_info(book, categories):

    categoryId = book['categoryId'] # print(type(categoryId))=<class 'list'>
    categoryName = []

    for category in categories: # print(type(category))=<class 'dict'>
        if category['id'] in categoryId:
            categoryName.append(category['name'])

    keys = ['id','title','author','priceSales','description','cover']

    my_book_info = {} # print(type(my_book_info))=<class 'dict'>

    for key in keys:
        my_book_info[key] = book[key]

    my_book_info['categoryName'] = categoryName

    return my_book_info

###############################################################################
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    book_json = open('data/book.json', encoding='utf-8')
    book = json.load(book_json)

    categories_json = open('data/categories.json', encoding='utf-8')
    categories_list = json.load(categories_json)

    pprint(book_info(book, categories_list))
