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