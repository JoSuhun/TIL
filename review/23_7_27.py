# class 상속

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def talk(self):
        print(f'안녕, {self.name}입니다.')

class Professor(Person):
    def __init__(self, name, age, department):
        # Person.__init__(self, name, age)
        super().__init__(name, age)
        self.department = department

class Student(Person):
    def __init__(self, name, age, gpa):
        super().__init__(name, age)
        self.gpa = gpa


p1 = Professor('조수훈', '73', 'ccccc')
p2 = Student('수훈이', '22', 'dede')

p1.talk()
p2.talk()

# -----------------------------------------

class Family:    
    def __init__(self, name):
        self.name = name
    
    def greeting(self):
        return f'안녕, 나는 {self.name}'
    

class Mom(Family):
    def __init__(self, name):
        super().__init__(name)

    gene = 'XX'

    def swim(self):
        return '엄마가 수영한다'


class Dad(Family):
    def __init__(self, name):
        super().__init__(name)

    gene = 'XY'

    def walk(self):
        return '아빠가 걷는다'
    

class FirstChild(Dad,Mom):      # 상속 순서 중요하다
    mom_gene = Mom.gene

    def __init__(self, name):
        super().__init__(name)

    def swim(self):
        return '첫째가 수영한다'
    
    def cry(self):
        return '첫째가 응애한다'
    

baby1 = FirstChild('아가예요')
print(baby1.cry())      # 첫째가 응애한다
print(baby1.swim())     # 첫째가 수영한다
print(baby1.walk())     # 아빠가 걷는다
print(baby1.gene)       # XY    # 상속 순서가 중요한 이유!
# print(baby1.mom_gene)   # XX

print(FirstChild.mro())
"""[<class '__main__.FirstChild'>,
<class '__main__.Dad'>, <class '__main__.Mom'>,
<class '__main__.Family'>, <class 'object'>]"""

# ----------------------------------------------------

# Errors & Exception

# debugging

# error

# try-excopt

# while True:
#     try:
#         a, b = map(int, input().split())
#         print(a+b)
#     except:
#         break

try:
    result = 10 / 0
except ZeroDivisionError:
    print('0으로 나눌 수 없어!!!')

try:
    num = int(input('100으로 나눌 값을 입력해!!!: '))
    print(100 / num)
except ValueError:
    print('숫자를 넣어야지')
except ZeroDivisionError:
    print('0은 넣지 말아야지')
except:
    print('에러야')

try:
    num = int(input('100으로 나눌 값을 입력해!!!: '))
    print(100 / num)
except BaseException:
    print('숫자를 넣어야지')
except ZeroDivisionError:
    print('0은 넣지 말아야지')
except:
    print('에러야')