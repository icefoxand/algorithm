# ws_5_1.py

# 아래 함수를 수정하시오.
# > 방법1
# def reverse_string1(ss):
#     sss = ''
#     for s in ss:
#         sss = s + sss
#     return sss
#
# result1 =reverse_string1("Hello, World!")
# print(result1)
#
# # > 방법2
# def reverse_string2(str):
#     return "".join(reversed(str))
#
# result2 = reverse_string2("Hello, World!")
# print(result2)

# ws_5_2.py

# 아래 함수를 수정하시오.
# > 방법1
# def remove_duplicates(arr):
#     new_lst = []
#     for el in arr:
#         if el not in new_lst:
#             new_lst.append(el)
#     return new_lst
#
# result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
# print(result)

# ws_5_3.py

# 아래 함수를 수정하시오.
# > 방법1
# new_tuple = ()
# def sort_tuple(tpl):
#
#     new_tuple = sorted(tpl)
#
#     return new_tuple
#
# result = sort_tuple((5, 2, 8, 1, 3))
# print(result)
#
# > 방법1
# lst = [5,4,3,2,1]
# i = 0
# A=''
# A = A.join(map(str,lst))
#
# print(A)
#
# > 방법2
# lst = [5,4,3,2,1]
# def fn(lst):
#     B = ''
#     for j in lst:
#         B += str(j)
#     return B
#
# print(fn(lst))

# hw_5_2.py
# def count_character(str,char):
#     result_str = str.count(char)
#     return result_str
#
# result = count_character("Hello, World!", "o")
# print(result) # 2

# hw_5_4.py
# def find_min_max(lst):
#     srt = sorted(lst)
#     return srt[0],srt[-1]
#
# result = find_min_max([3, 1, 7, 2, 5])
# print(result) # (1, 7)

# ws_5_5.py

# 아래 함수를 수정하시오.
# def even_elements(lst):
#     new_list = []
#     for _ in range(len(lst)):
#         a = lst.pop(0)
#         if a % 2 == 0:
#             new_list.extend([a])
#
#     return new_list
# my_list = [1,2,3,4,5,6,7,8,9,10]
# result = even_elements(my_list)
# print(result)

# ws_6_1.py
# set1=()
# set2=()
# def union_sets(set1,set2):
#     sets = set1.union(set2)
#     return sets
# result = union_sets({1, 2, 3}, {3, 4, 5})
# print(result)
# blood_types=['A','B','A','O','AB','AB','O','A','B','O','B','AB']
# new_dict={}
# for blood_type in blood_types:
#     # 기존에 키가 이미 존재한다면,
#     if blood_type in new_dict:
#         # 기존 키의 값을 +1 증가시킨다.
#         new_dict[blood_type] += 1
#     # 키가 존재하지 않는다면(=지금부터 처음 설정되는 키)
#     else:
#         new_dict[blood_type] = 1
# print(new_dict)
# #####
# blood_types=['A','B','A','O','AB','AB','O','A','B','O','B','AB']
# new_dict={}
# for blood_type in blood_types:
#     # 기존에 키가 이미 존재한다면,
#     new_dict[blood_type] = new_dict.get(blood_type,0) + 1
# print(new_dict)
# #####
# blood_types=['A','B','A','O','AB','AB','O','A','B','O','B','AB']
# new_dict={}
# for blood_type in blood_types:
#     new_dict.setdefault(blood_type, 0)
#     new_dict[blood_type] += 1
# print(new_dict)
#####
# ws_6_2.py

# 아래 함수를 수정하시오.
# dic = ()
# n =''
# my_dict = {'name': 'Alice', 'age': 25}
# def get_value_from_dict(dic,n):
#     return dic.get(n)
#
# result = get_value_from_dict(my_dict, 'name')
# print(result) # Alice
# ws_6_3.py

# 아래 함수를 수정하시오.
# def intersection_sets(set1,set2):
#     return set1.intersection(set2)
#
# result = intersection_sets({1, 2, 3}, {3, 4, 5})
# print(result) # {3}
# ws_6_4.py

# 아래 함수를 수정하시오.
# my_dict = {'name': 'Alice', 'age': 25}
# dic ={}
#
# def get_keys_from_dict(dic):
#     return dic.keys()
#
# result = get_keys_from_dict(my_dict)
# print(result)
# ws_6_5.py

# 아래 함수를 수정하시오.
# set1=()
# set2=()
# def difference_sets(set1,set2):
#     return set1.difference(set2)
#
# result = difference_sets({1, 2, 3}, {3, 4, 5})
# print(result)

# hw_6_2.py
# 아래 함수를 수정하시오.
# lst=[]
# def remove_duplicates_to_set(lst):
#     return set(lst)
#
# result = remove_duplicates_to_set([1, 2, 2, 3, 4, 4, 5])
# print(result)
# hw_6_4.py

# 아래 함수를 수정하시오.
# dic={}
# d={}
# def add_item_to_dict(dic,key,value):
#     new_dict = dic.copy()
#     for d in new_dict:
#         new_dict.setdefault(key,value)
#         return new_dict
# my_dict = {'name': 'Alice', 'age': 25}
# result = add_item_to_dict(my_dict, 'country', 'USA')
# print(result)
# ws_5_4.py

# 아래 함수를 수정하시오.
# str = ''
# def capitalize_words(str):
#     return str.title()
#
# result = capitalize_words("hello, world!")
# print(result)

# 절차지향
# 로또번호 생성기
# import random
# lotto_nums = []
# for i in range(6):
#     ran_num = random.randint(1,45)
#     if ran_num in lotto_nums:
#         continue
#     lotto_nums.append(ran_num)
# # 만들어내고나서 정렬
# lotto_nums.sort()
# print(lotto_nums)

# 객체지향
# 로또번호생성 프로그램 작성하고싶다~
# 로또번호생성 하는 애가 있어야 한다~
# 로또번호정렬 하는 애도 있어야 한다~
# 로또번호생성 하는 애가 정렬도 할 수 있어야한다~
#
# class LottoNumberMaker:
#     def __init__(self):
#         self.lotto_nums = []
#         pass
#     def create_number():
#         while len(self.lotto_num)
#         pass
#     def lotto_sort(self):
#         pass

# 모듈화한다 = 비슷하게 작동하는 작은것들을 뭉쳐서 하나의 큰 덩어리로 만들기
# 코드의 재사용성, 코드의 활용성, 코드의 가시성 높이기
# ws_7_1.py

# 아래 클래스를 수정하시오.
# class Shape:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
# shape1 = Shape(5, 3)
# print(shape1.width, shape1.height)
# ws_7_2.py

# 아래 클래스를 수정하시오.
# class Shape():
#     def __init__(self,w,h):
#         self.w = w
#         self.h = h
#     def calculate_area(self):
#         return f'{self.w * self.h}'
# shape1 = Shape(5, 3)
# area1 = shape1.calculate_area()
# print(area1)
# ws_7_3.py

# 아래 클래스를 수정하시오.
# class Shape:
#    def __init__(self,w,h):
#        self.w=w
#        self.h=h
#    def calculate_perimeter(self):
#        return f'2{self.w + self.h}'
#
# shape1 = Shape(5, 3)
# perimeter1 = shape1.calculate_perimeter()
# print(perimeter1)
# ws_7_4.py

# 아래 클래스를 수정하시오.
# class Shape:
#    def __init__(self,w,h):
#        self.w = w
#        self.h = h
#    def calculate_area(self):
#        return self.w * self.h
#    def calculate_perimeter(self):
#        return 2 * self.w + 2 * self.h
#    def print_info(self):
#        print("Width: ",self.w)
#        print("Height: ",self.h)
#        print("Area: ",self.calculate_area())
#        print("Perimeter: ",self.calculate_perimeter())
# shape1 = Shape(5, 3)
# shape1.print_info()

# ws_7_5.py

# 아래 클래스를 수정하시오.
# class Shape:
#    def __init__(self,w,h):
#        self.w = w
#        self.h = h
#    def __str__(self):
#        return f'Shape: width={self.w}, height={self.h}'
# shape1 = Shape(5, 3)
# print(shape1)

# hw_7_2.py

# 아래 클래스를 수정하시오.
# hw_7_2.py

# 아래 클래스를 수정하시오.
# class StringRepeater:
#    def __str__(self,n,z):
#        self.n = n
#        self.z = z
#    def repeat_string(self,n,z):
#        for i in range(n):
#            print(z)
#
# repeater1 = StringRepeater()
# repeater1.repeat_string(3, "Hello")
# hw_7_4.py

# 아래 클래스를 수정하시오.
# class Person:
#
#     number_of_people = 0
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         Person.number_of_people += 1
#
#     def introduce(self):
#         print(f'제 이름은{self.name}이고, 저는 {self.age}살 입니다.')
#
# person1 = Person("Alice", 25)
# person1.introduce()
# print(Person.number_of_people)
# ws_8_1.py

# 아래 클래스를 수정하시오.
# print('❤❤❤❤❤')
# class Animal:
#     number_of_animal = 0
#     def __init__(self):
#         Animal.number_of_animal += 1
#
# class Dog(Animal):
#     def __init__(self):
#         self.Dog = Dog
#         Animal.number_of_animal += 1
#
# class Cat(Animal):
#     def __init__(self):
#         self.Cat = Cat
#         Animal.number_of_animal += 1
#
# class Pet(Dog, Cat):
#     def __init__(self):
#         self.Pet = Pet
#     def access_num_of_animal():
#         return f'동물의 수는 {Pet.number_of_animal}마리 입니다.'
#
# dog = Dog()
# print(Pet.access_num_of_animal())
# cat = Cat()
# print(Pet.access_num_of_animal())

###상속이란?_class diagram 으로 표현해보자!

# class Person:
#     greeting = "Hello"
#
# class Student(Person):
#     pass
# class Professor(Person):
#     pass
# def say_hello(person):
#     person.talk()
#
# s1 = Student()
# p1 = Professor()
# s1.talk()
# p1.talk()


# ws_8_2.py

# 아래 클래스를 수정하시오.
# class Animal:
#     def __init__(self):
#         self.Animal = Animal
#
# class Dog(Animal):
#     def __init__(self):
#         self.Dog = Dog
#
#     def bark(self):
#         return print('멍멍!')
#
# dog1 = Dog()
# dog1.bark()

# ws_8_3.py

# # 아래 클래스를 수정하시오.
# class Animal:
#     def __init__(self):
#         self.Animal = Animal
#
# class Cat(Animal):
#     def __init__(self):
#         self.Cat = Cat
#     def meow(self):
#         return print('야옹!')
#
# cat1 = Cat()
# cat1.meow()

# class Dog:
#     def __init__(self):
#         self.Dog = Dog
#     def bark(self):
#         print('멍멍!')
#
# class Cat:
#     def __init__(self):
#         self.Cat = Cat
#     def meow(self):
#         print('야옹!')
#
# class Pet(Dog, Cat):
#
#     def __init__(self,sound):
#         self.Pet = Pet
#         self.sound = sound
#
#     def make_sound(self):
#         print(f'{self.sound}')
#
#     @staticmethod
#     def play():
#         print('애완동물과 놀기')
#
# pet1 = Pet("그르르")
# pet1.make_sound()
# pet1.bark()
# pet1.meow()
# pet1.play()


# ws_8_5.py
# Dog class와 Cat class를 다중상속받는 Pet class
# Pet class에는 __str__ 매직 메서드를 추가하고 객체를 문자열로 표현
# Dog 와 Cat는 각각 sound(클래스속성)을 가지며 각 동물의 소리를 나타낸다
# Pet class는 Dog, Cat 을 다중상속 받아야함
# __str__를 오버라이딩 하여 Pet객체를 문자열로 표현할수있게
# __str__메서드는 "애완동물은 {소리}소리를 냅니다."형식으로 반환
# Dog Class를 우선 상속시: "애완동물은 멍멍 소리를 냅니다."
# Cat Class를 우선 상속시: "애완동물은 야옹 소리를 냅니다."
#
#  class Dog:
#      def __init__(self,sound):
#             self.sound=sound
# class Cat:
#     def __init__(self,sound):
#
# class Pet(Dog, Cat):
#     def __str__(self,sound):
#         self.sound = sound
#         super().__str__()
#         print(f'애완동물은 {소리}소리를 냅니다')
##########################
# try:
#     result = my_dict['key']
#     print(result)
#
# except KeyError:
#     print('Key가 존재하지 않습니다.')
#
# if 'key' in my_dict:
#     result = my_dict['key']
#     print(result)
#
# else:
#     print('Key가 존재하지 않습니다.')
######################################
# class Dog:
#     sound = "멍멍"
#
#     def __init__(self):
#         self.Dog = Dog
#
#
# class Cat:
#     sound = "야옹"
#
#     def __init__(self):
#         self.Cat = Cat
#
#
# class Pet(Dog, Cat):
#
#     def __init__(self):
#         self.Pet = Pet
#         super().__init__()
#
#     def __str__(self):
#         return f'애완동물은 {self.sound} 소리를 냅니다.'
#
#
# pet1 = Pet()
# print(Pet.__str__(Pet))
#############################

# hw_8_2.py

# 아래 함수를 수정하시오.

# r=''
# def check_number(r):
#     try:
#         if float(r) >= 0 :
#             print('양수입니다')
#         else:
#             float(r) < 0
#             print('음수입니다')
#     except ValueError:
#         return print('잘못된 입력입니다')
#
# check_number()
##################
# hw_8_4.py

# 아래 클래스를 수정하시오.
class UserInfo:
    def __init__(self):
        self.user_data = {}

    def get_user_info(self):
        pass

    def display_user_info(self):
        pass

user = UserInfo()
user.get_user_info() # 이름과 나이를 입력받는 메서드
user.display_user_info() # 이름과 나이를 출력하는 메서드
