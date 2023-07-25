# [세트 메서드]
my_set = {1,2,3}
my_set.discard(2)

print(my_set)

my_set.discard(10)
print(my_set)
# my_set.remove(10)         # Error

element = my_set.pop()
print(element)
print(my_set)

# [dictionary 메서드]
my_dict = {
    'name' : 'suhunida'
}

print(my_dict['name'])
print(my_dict.get('name'))

# print(my_dict['age'])         # Error, 이후 코드 멈춤
print(my_dict.get('age', 'Unknown'))    # 키의 값이 없어도, 이후 코드는 계속


person = {
    'name': 'suhunida',
    'age' : 35
}

# print(person.keys())

# for key in person.keys():
#     print(key)
#     """
#     name
#     age
#     """

# for key, value in person.items():
#     print(key, value)
#     """
#     name suhunida
#     age 35"""

# person = {
#     'name': 'suhunida',
#     'age' : 35
# }

# print(person.setdefault('country,', 'KOREA'))       # KOREA
# print(person)       # {'name': 'suhunida', 'age': 35, 'country,': 'KOREA'}

person = {
    'name': 'suhunida',
    'age' : 35
}

person.update(age=27)

print(person)       # {'name': 'suhunida', 'age': 27}



# 세가지 방법으로 딕셔너리 이용하기

# 1. []
# 2. .get()
# 3. .setdefault()

# 혈액형 인원수 세기
blood_types = ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']

# 1. []
new_dict = {}

for blood_type in blood_types:
    # 기존에 키가 이미 존재한다면
    if blood_type in new_dict:
        new_dict[blood_type] += 1
    # 키가 존재하지 않는다면 (처음 들어오는 키)
    else:
        new_dict[blood_type] = 1

print(new_dict)

# 2. .get() ##!
new_dict = {}

for blood_type in blood_types:
    new_dict[blood_type] = new_dict.get(blood_type, 0) +1

print(new_dict)

# 3. .setdefault()  #### !!!
new_dict = {}

for blood_type in blood_types:
    new_dict.setdefault(blood_type, 0)
    new_dict[blood_type] += 1

print(new_dict)


# 얕은 복사

a = [1,2,3]

# 슬라이싱
b = a[:]
b[0] = 100
print(a, b)     # [1, 2, 3] [100, 2, 3]
# copy
c = a.copy()
c[0] = 100
print(a, c)     # [1, 2, 3] [100, 2, 3]

# 얕은 복사의 한계 
a = [1, 2, [1, 2]]

b = a[:]
b[2][0] = 999
print(a, b)     # [1, 2, [999, 2]] [1, 2, [999, 2]]


# 깊은 복사
import copy

original_list = [1, 2, [1, 2]]

deep_copied_list = copy.deepcopy(original_list)

deep_copied_list[2][0] = 999

print(original_list, deep_copied_list)