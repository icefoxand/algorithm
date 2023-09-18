import json

def best_book(books):
    # 0-0. 인덱싱으로 사용할 id값의 리스트 만들기
    books_json = open('data/books.json', encoding='utf-8')
    books_list = json.load(books_json)

    # 0-1. list comprehension 으로 리스트 만들기
    Id_list = [Ids['id'] for Ids in books_list]

    # 1-0. books 라는 json파일이 들어가면, my_best_book이라는 결과가 나오는 함수 만들기
    books_list_files = []
    for i in range(len(Id_list)):
        I = Id_list[i]
        books_json_files = open(f"data/books/{I}.json",encoding='utf-8')
        books_dict_files = json.load(books_json_files)
        books_list_files.append(books_dict_files)

    best_number = [c['customerReviewRank']for c in books_list_files]
    best_book_idx = best_number.index(max(best_number))
    my_best_book = books_list[best_book_idx]

    return my_best_book['title']


    # return my_best_book



# 아래의 코드는 수정하지 않습니다. #################################################################
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books_list = json.load(books_json)

    print(best_book(books_list))
