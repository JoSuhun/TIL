# 클래스 정의
class Person:
    # 속성(변수)
    blood_color = 'red'

    # 메서드
    def __init__(self,name):
        self.name = name
    # __매직메서드__ : 개발자가 직접 호출하지 않음
    # __init__ : 초기화, 생성자 메서드
    
    # 인스턴스 메서드
    def singing(self):
        return f'{self.name}가 노래합니다.'
    
# 인스턴스 생성
singer1 = Person('spitz')
singer2 = Person('backnumber')

# 메서드 호출
print(singer1.singing())
print(singer2.singing())

# 속성(변수) 사용
print(singer1.blood_color)
print(singer2.blood_color)


# 데일리과제 7-4
class Person:
   number_of_people =0

   def __init__(self, name, age):
      self.name = name
      self.age = age
      Person.number_of_people +=1

   def introduce(self):
      print(f'제 이름은 {self.name}이고, 저는 {self.age}살 입니다.')

person1 = Person("Alice", 25)
person1.introduce()
print(Person.number_of_people)


# Review (^ - ^)

# 매직 메서드

class car:
    def __init__(self,name,price):
        self.name = name
        self.price = price
    
    def __add__(self,another):
        return self.price + another.price

kia = car('k8',500)
bmw = car('m8',100)

print(kia.price + bmw.price)

# deco

def deco(fnc):
    def wrapper(value):
        print('뉴진스'*3)
        fnc(value)
        print('하입보이'*3)
    return wrapper

@deco
def call_name(name):
    print(name)

@deco
def call_age(age):
    print(age)

call_name('수훈이')

# 정적 메서드

class car:

    @staticmethod
    def add_price(one, another):
        print(one+another)

car.add_price(400, 80000)

# 클래스 메서드

class make_pie:
    cnt = 0
    def __init__(self, name):
        self.name = name
        make_pie.cnt+=1
    
    @classmethod
    def number_of_pies(cls):
        print(f'파이를 {cls.cnt}명이 만들고 있다 ㅇㅅㅇ')

a = make_pie('sh')
b = make_pie('hs')
make_pie.number_of_pies()