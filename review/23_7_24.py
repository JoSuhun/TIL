# [문자열 메서드]

# .isalpha()
string = 'Hello'
print(string.isalpha())

# .strip()
text = '         HAHA HAHAHA        '
new_text = text.strip()
print(new_text)

# [리스트 메서드]

# .append()
numbers = [1, 2, 3]
numbers2 = [4, 5, 6]
numbers.append(numbers2)
print(numbers)       # [1, 2, 3, [4, 5, 6]]

# .extend()
numbers.extend(numbers2)
print(numbers)      # [1, 2, 3, 4, 5, 6]

# .insert()
my_list = [1, 2, 3]
my_list.insert(1,[5, 5, 5])
print(my_list)      # [1, [5, 5, 5], 2, 3]

# .remove()
my_list2 = [1, 2, 3, 4, 2]
my_list2.remove(2)
print(my_list2)      # [1, 3, 4, 2]

# .pop()
my_list3 = [1, 2, 3, 4, 5]

item1 = my_list3.pop()
item2 = my_list3.pop(0)

print(item1)        # 5
print(item2)        # 1
print(my_list3)      # [1, 3, 4, 2]

# .sort()
my_list_sort = [3, 2, 1]
# sort 오름차순
my_list_sort.sort()
print(my_list_sort)         # [1, 2, 3]

# sort 내림차순
my_list_sort.sort(reverse = True)
print(my_list_sort)         # [3, 2, 1]

# (추가) sorted 내장함수
my_list_sort_2 = [3, 2, 1]

print(my_list_sort_2.sort())    # None -- 메서드임. 원본을 바꾸고 return을 안 한다
print(sorted(my_list_sort_2))   # [1, 2, 3] -- 함수임. 복사본을 만들고 return을 한다

# .reverse()
my_list_rev = [1,3,2,6,8,9]
my_list_rev.reverse()
print(my_list_rev)          # [9, 8, 6, 2, 3, 1]

# (추가) list 할당과 주소 복사
list_ = []
numbers = [1, 2, 3]

# 할당
list1 = numbers
# 슬라이싱
list2 = numbers[:]

numbers[0] = 100
print(list1)        # [100, 2, 3]
print(list2)        # [1, 2, 3]




# [[review]]


#'a'가 있는곳의 인덱스 / 없으면 -1
st='apple,banana,mango'

index=st.find('a',1) 
print(index)        # 7

#'p'가 있는곳의 인덱스 / 없으면 버그
alpha=st.index('p')
print(alpha)        # 1

# join 합치기 

st=['a','p','p','l','e']    
str2="".join(st)

print(str2)         # apple

# 리스트 안에 문자를 합치는데 사이사이에 ,를 넣어라
st=['apple','banana','mango']
str2=','.join(st)
print(str2)         # apple,banana,mango

# 대문자, 소문자
st='apple,banana,mango'
str2=st.upper()
print(str2)     # APPLE,BANANA,MANGO

str2=st.lower()
print(str2)

# 입력값 소문자로 변환
st='HEodJEW'.lower().split()
print(st)

# 문자 교체하기
st='apple '
str2=st.replace('ap','ma')
print(str2)

# -------------------------------------------------------
# -------------------------------------------------------


# 리스트 값 추가하기
st=['apple','banana','mango']
st.append('ornage')
print(st)

# 리스트 값 삽입
st.insert(1,'orange')
print(st)

# 리스트 확장
st=[1,2,3]
str2=[4,5]
st.extend(str2)
print(st)       # [1,2,3,4,5]

st+=str2    # 또는, 리스트끼리 더해버려
print(st)       #[1,2,3,4,5,4,5]

# 값 삭제 (pop 속 비워두면 마지막요소 삭제)
st.pop()
print(st)       # [1,2,3,4,5,4]

# 값 삭제 (배열에서 첫번째로 나오는 값이 삭제됨)
st.remove(4)        # [1,2,3,5,4]
print(st)

# 값 삭제 (del 함수)
del st[3:]
print(st)       # [1,2,3]
del st[1]       # [1,3]
print(st)

# 값 삭제, 리스트 비워버려 몽땅 다 삭제
st.clear()
print(st)       # [] 없어..

# reverse 역순으로 재배열
st=[1,2,3,4,5]
st.reverse()
print(st)       # [5, 4, 3, 2, 1]

st=st[::-1]
print(st)       # [1, 2, 3, 4, 5]

# sort 정렬
a1=[6,3,9]

a1.sort()
print(a1)       # [3, 6, 9]

a1.sort(reverse=True)
print(a1)       # [9, 6, 3]


a1=[6,3,9]
ret=sorted(a1) # 메서드가 아닌 함수 sorted!! 원본 데이터 유지하고 새로이 반환함
print(a1,ret)
ret=sorted(a1,reverse=True)
print(ret)


a1='asdf'
# a1.sort()
# print(a1)
# # a1.sort() 동작 안함 
# # (a1이 가르키고 있는 곳의 주소값이 맨 앞글자 'a'가 저장되어 있는곳의
# # (주소값을 가르키기 때문에 원본 데이터를 바꾸면 안됨)

a1=sorted(a1) # ['a', 'd', 'f', 's'] 함수 sorted로 반환하여 배열하는 것은 가능하다!!
print(a1)
a1=''.join(a1)
print(a1)

###@@@# lambda 를 이용한 리스트 정렬
lst=list(range(10))
ret = sorted(lst, key = lambda x : x)
ret2 = sorted(lst, key = lambda x : x , reverse = True)
ret3 = sorted(lst, key = lambda x : -x)

print(ret)      # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(ret2)     # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(ret3)     # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]


lst=[(3,'banana'),(2,'apple'),(1,'carrot')]
ret1 = sorted(lst, key = lambda x : x[1])
ret2 = sorted(lst, key = lambda x : x[1], reverse = True)
ret3 = sorted(lst, key = lambda x : x[0])


print(ret1)       # [(2, 'apple'), (3, 'banana'), (1, 'carrot')]
print(ret2)       # [(1, 'carrot'), (3, 'banana'), (2, 'apple')]
print(ret3)       # [(1, 'carrot'), (2, 'apple'), (3, 'banana')]