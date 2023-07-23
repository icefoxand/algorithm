
import ws5_book
name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]

def create_user(name, age):   
    print(f'{name}님 환영합니다')
    user_info = {}
    user_info['name'] = name
    user_info['age'] = age              
    return user_info

many_user = list(map(create_user, name, age))
def rental_book(info):
    n = info['age'] // 10
    ws5_book.decrease_book(n)
    print(f'{info["name"]}님이 {n}권의 책을 대여하였습니다.')

dic_info = list(map(lambda info: rental_book(info), many_user)) 