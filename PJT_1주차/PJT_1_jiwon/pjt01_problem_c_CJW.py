import json
from pprint import pprint

def books_info(books, categories):

    result_of_book_info = []
    
    for item_books in books:
        new_dic = {}
        key_list = ['id', 'title', 'author', 'priceSales', 'description', 'cover']
        for key in key_list:
            new_dic[key] = item_books[key]

        categoryIds = item_books['categoryId']
        categoryName = []
        # #
        for category in categories:
            if category['id'] in categoryIds:
                categoryName.append(category['name'])

        new_dic['categoryName'] = categoryName
        result_of_book_info.append(new_dic)

    return result_of_book_info
        

##########################################################################
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books = json.load(books_json)

    categories_json = open('data/categories.json', encoding='utf-8')
    categories_list = json.load(categories_json)

    pprint(books_info(books, categories_list))