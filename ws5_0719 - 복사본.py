# 실습 번호.py
import ws5_book         # book.py에서 함수와 책의 갯수 불러오기

name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]

def create_user(name, age):   
    print(f'{name}님 환영합니다')        # 결과값에 나타날 print문
    user_info = {}                      # 빈 딕셔너리 생성
    user_info['name'] = name            # 딕셔너리 key-value 추가
    user_info['age'] = age              
    return user_info                    # 딕셔너리 반환

# map 함수로 딕셔너리를 리스트로 반환
many_user = list(map(create_user, name, age)) 
# print(many_user)              # 결과값을 모르겠다면 주석처리를 지우고 출력값 확인해 볼 것!!

def rental_book(info):
    n = info['age'] // 10       # info라는 딕셔너리의 'age'의 value를 불러와 n을 정의
    ws5_book.decrease_book(n)   # book.py 파일의 decrease 함수 사용 -> 책의 수 감소, print문 실행
    print(f'{info["name"]}님이 {n}권의 책을 대여하였습니다.')

# many_user(리스트)에서 딕셔너리 하나하나를 info 변수로 만들어 rental_book 함수를 실행
dic_info = list(map(lambda info: rental_book(info), many_user)) 