# 선택 정렬
arr = [4, 7, 1, 3, 5]

for y in range(len(arr)-1):
    for x in range(y+1, len(arr)):
        if arr[y] > arr[x]:
            arr[y], arr[x] = arr[x], arr[y]

print(arr)


# 삽입 정렬
arr = [4, 7, 1, 3, 5]

result = [0]*5

for i in range(len(arr)):
    result[i] = arr[i]
    for j in range(i, 0, -1):
        if result[j-1] > result[j]:
            result[j-1] , result[j] = result[j] , result[j-1]
        else:
            break

print(result)


# 버블 정렬
arr = [8, 3, 12, 10, 1]

for i in range(len(arr)-1 , 0, -1):
    for j in range(i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print(arr)