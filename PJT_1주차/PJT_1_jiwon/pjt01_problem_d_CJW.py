import json
from pprint import pprint

def sorted_cs_books_by_price(books, categories):
    sorted_cs_books_rank = 0
    sorted_cs_books_title =''

    for book in books:
        data = open("data/books/",encoding='UTF8')
        book = json.load(data)

        if sorted_cs_books_rank < book_detail_list['customerReviewRank']:
            sorted_cs_books_rank = book_detail_list['customerReviewRank']
            sorted_cs_books_title < book_detail_list['title']

    return sorted_cs_books_title


####################################################################
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books = json.load(books_json)

    categories_json = open('data/categories.json', encoding='utf-8')
    categories_list = json.load(categories_json)

    print(sorted_cs_books_by_price(books, categories_list))
