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