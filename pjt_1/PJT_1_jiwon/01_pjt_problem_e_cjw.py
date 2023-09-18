import json


def new_books(books):
    # 0-0. 인덱싱으로 사용할 id값의 리스트 만들기
    books_json = open('data/books.json', encoding='utf-8')
    books_list = json.load(books_json)
    # print(books_list)

    # 0-1. list comprehension 으로 리스트 만들기
    Id_list = [Ids['id'] for Ids in books_list]
    # print(Id_list)

    # 1-0. books 라는 json파일이 들어가면, my_best_book이라는 결과가 나오는 함수 만들기
    books_list_files = []
    for i in range(len(Id_list)):
        I = Id_list[i]
        books_json_files = open(f"data/books/{I}.json", encoding='utf-8')
        books_dict_files = json.load(books_json_files)
        books_list_files.append(books_dict_files)

    p1 = [c['pubDate'][:4] for c in books_list_files]

    p2 = []
    if '2023' in p1:
        p2.append(p1)
        print(p2)

    # new_data =



# 아래의 코드는 수정하지 않습니다.##############################
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books_list = json.load(books_json)
    
    print(new_books(books_list))
