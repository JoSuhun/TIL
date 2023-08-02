# enumerate

fruits = ['apple', 'banana', 'cherry']
print(list(enumerate(fruits)))
# [(0, 'apple'), (1, 'banana'), (2, 'cherry')]
# 리스트의 인덱스와 값을 튜플로 묶어줘!!!!!

for index, fruit in enumerate(fruits):
    print(f'인덱스 {index}: {fruit}')
    """
    인덱스 0: apple
    인덱스 1: banana
    인덱스 2: cherry
    """
# fruits리스트의 'cherry'가 몇 번째 인덱스인지 알고싶다!!
for index, fruit in enumerate(fruits):
    if fruit == 'cherry':
        print(index)    # 2 ... 알고리즘 풀이에 유용할 거 같음
