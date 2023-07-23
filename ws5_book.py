# book.py
number_of_book = 100

def decrease_book(n):
    global number_of_book
    number_of_book -= n
    print(f'남은 책의 수 : {number_of_book}')
