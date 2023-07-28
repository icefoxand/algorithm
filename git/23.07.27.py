# class parrent:

#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def talk(self):
#         print(f'나는{self.name}입니다')


# class child_girl(parrent):

#     def __init__(self,name,age,department):
#         self.name = name
#         self.age = age
#         self.department = department


# class child_boy(parrent):

#     def __init__(self,name,age,gpa):
#         self.name = name
#         self.age = age
#         self.gpa = gpa
#
# n2_a = child_girl('최',30,'정책학과')
# n2_b = child_boy('김',20,'화학과')
#
# n2_a.talk()
# n2_b.talk()
# print('❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤')
#
# class parrent:
#     def __init__(self,name,age,number,email):
#         self.name = name
#         self.age = age
#         self.number = number
#         self.email = email
#
# class child_boy(parrent):
#     def __init__(self,name,age,number,email,id):
#         self.name = name
#         self.age = age
#         self.number = number
#         self.email = email
#         self.id = id
#
# n2_b = child_boy('김',20,'화학과')
# print('❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤')
#
# class Parrent:
#     def __init__(self,name,age,number,email):
#         self.name = name
#         self.age = age
#         self.number = number
#         self.email = email
#
#
# class Child(Parrent):
#     def __init__(self,name,age,number,email,id):
#         super().__init__(name,age,number,email)
#         self.id=id

class Parrent:
    def __init__(self,name):
        self.name = name
    def greeting(self):
        return f'안녕,나는{self.name}'

class Child_girl(Parrent):
    gene = 'XX'
    def swim(self):
        return '딸이 수영한다'

class Child_boy(Parrent):
    gene = 'YY'
    def walk(self):
        return '아들이 걷는다'

class Super_child(Child_boy,Child_girl):
    def swim(self):
        return '손녀가 수영한다'
    def cry(self):
        return '손녀가 운다'

super = Super_child('손녀')
print(super.cry())
print(super.swim())
print(super.walk())
print(super.gene)