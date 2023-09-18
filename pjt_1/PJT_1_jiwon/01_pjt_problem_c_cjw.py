import json
from pprint import pprint


def books_info(books, categories):

    my_books_info = []
    
    for a_book in books:
        new_dic_1 = {}
        keys = ['id', 'title', 'author', 'priceSales', 'description', 'cover']
        for key in keys:
            new_dic_1[key] = a_book[key]
        categoryIds = a_book['categoryId']
        categoryName = []
        for category in categories:
            if category['id'] in categoryIds:
                categoryName.append(category['name'])
        new_dic_1['categoryName'] = categoryName

        my_books_info.append(new_dic_1)

    return my_books_info
        

##########################################################################
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books = json.load(books_json)

    categories_json = open('data/categories.json', encoding='utf-8')
    categories_list = json.load(categories_json)

    pprint(books_info(books, categories_list))