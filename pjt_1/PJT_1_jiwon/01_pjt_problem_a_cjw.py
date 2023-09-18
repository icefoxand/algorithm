import json
from pprint import pprint


def book_info(book):
    # 필요정보(id,name,author,priceSales,description,cover,categoryID)를
    # 필요정보만 꺼내서, 새로운 딕셔너리로 반환할 새로운 함수, 'book_info()'.

    # 0. 필요한 키 종류를 list에 담아주기
    keys = ['id','title','author','priceSales','description','cover','categoryId']

    # 1. 새로운 딕셔너리를 선언하기
    my_book_info = {}

    # 2. 키 리스트에 해당하는 정보만 추출(for문 사용)
    for key in keys:
        my_book_info[key] = book[key]

    # 3. 새롭게 재가공한 딕셔너리로 반환
    return my_book_info

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__': # 이거 이터레이터로 만들어주는 형태임. 즉 이터레이터가 뭔지 잘 알아야함.
    book_json = open('data/book.json', encoding='utf-8')
    book = json.load(book_json)
    
    pprint(book_info(book))
