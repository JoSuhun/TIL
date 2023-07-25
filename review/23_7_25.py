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

print(person.keys())

for key in person.keys():
    print(key)
    """
    name
    age
    """

for key, value in person.items():
    print(key, value)
    """
    name suhunida
    age 35"""

person = {
    'name': 'suhunida',
    'age' : 35
}

print(person.setdefault('country,', 'KOREA'))       # KOREA
print(person)       # {'name': 'suhunida', 'age': 35, 'country,': 'KOREA'}

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

print(original_list, deep_copied_list)      # [1, 2, [1, 2]] [1, 2, [999, 2]]



# REVIEW (^ - ^)

# [[set]] - 중복을 허용하지 않는

s = {1, 2, 3, 4, 5}

# set 값 추가
s.add(6)
print(s)        # {1, 2, 3, 4, 5, 6}

s.update([7,8,9])
print(s)         # {1, 2, 3, 4, 5, 6, 7, 8, 9}
# set 값 삭제
s.remove(9)
print(s)      # {1, 2, 3, 4, 5, 6, 7, 8}

# s.remove(999)
# print(s)      # KeyError

s.discard(9999)
print(s)      # {1, 2, 3, 4, 5, 6, 7, 8} remove와 달리 없으면 넘어감 Error없음

# 집합
s1 = [1, 2, 3, 4]
s2 = [2, 4, 6, 8]

s1, s2 = set(s1), set(s2)

# 교집합
print(s1 & s2)      # {2, 4}        # & : 엠퍼센드
print(list(s1 & s2))

# 합집합
print(s1 | s2)      # {1, 2, 3, 4, 6, 8}

# 차집합
print(s1 - s2)      # {1, 3}


# [[dictionary]]

st = {
    'kevin' : 1,
    'john' : 2,
    'suhun' : 3
}

# key, value를 추가하자
st['nana'] = 4
print(st)       # {'kevin': 1, 'john': 2, 'suhun': 3, 'nana': 4}

# key, value를 삭제하자
del st['nana']
print(st)       # {'kevin': 1, 'john': 2, 'suhun': 3}

# key or value만 추출하기
lst = st.keys()
print(lst)      # dict_keys(['kevin', 'john', 'suhun'])
print(list(lst))        # ['kevin', 'john', 'suhun']

# key와 value를 함께 추출하기
lst = st.items()
print(lst)      # dict_items([('kevin', 1), ('john', 2), ('suhun', 3)])
print(list(lst))        # [('kevin', 1), ('john', 2), ('suhun', 3)]

# key로 value 추출하기
print(st['suhun'])      # 3     # 없는 키를 넣었을 경우, Error
print(st.get('suhuniiii', '없어용'))      # 없는 키를 넣었을 경우, Error없이 None 혹은 default 반환

# 삭제 (del, pop)
st = {
    'kevin' : 1,
    'john' : 2,
    'suhun' : 3
}

st.pop('kevin')
print(st)       # {'john': 2, 'suhun': 3}

st.pop('qwer', 0)   # 없는 키를 넣었을 경우, default를 설정해주면 Error 없음.
print(st)       # {'john': 2, 'suhun': 3}


# <<추가학습 ㅇㅅㅇ>>
# counter - 중복된 데이터가 각각 몇개씩 있는지 알려줌
from collections import Counter

lst = ['apple', 'mango', 'banana','mango', 'apple', 'banana',
       'mango', 'suhuni']

print(Counter(lst))     # Counter({'mango': 3, 'apple': 2, 'banana': 2, 'suhuni': 1})

ret = dict(Counter(lst))
print(ret)      # {'apple': 2, 'mango': 3, 'banana': 2, 'suhuni': 1}

# (문제) 문자열 안에서 가장 많이 사용된 알파벳이 뭐야
st = 'an applemango'
print(Counter(st))      # Counter({'a': 3, 'n': 2, 'p': 2, ' ': 1, 'l': 1, 'e': 1, 'm': 1, 'g': 1, 'o': 1})

ret = dict(Counter(st))
ret = sorted(ret.items(), key = lambda x:x[1], reverse=True)
# x[1]인 알파벳별로 사용된 개수를 기준key으로 sort함
# reverse = True를 통해 내림차순 정렬
print(f'{ret[0][0]}가 {ret[0][1]}번 사용됨')        # a가 3번 사용됨

# (문제) 문자열 안에서 가장 많이 사용된 알파벳이 뭐야
# Counter안의 mostcommon메서드 이용
st = 'an applemango'
ret = Counter(st).most_common(1)        # most_common()안의 1은 1등을 말함
print(ret)      # [('a', 3)]
print(f'{ret[0][0]}가 {ret[0][1]}번 사용됨')        # a가 3번 사용됨

# 문자열의 덧셈과 뺄셈
a = Counter('apple')
b = Counter('mango')
print(a + b)
print(a - b)