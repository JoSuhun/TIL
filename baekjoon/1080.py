n, m = map(int,input().split())
arr1 = [list(map(int, input())) for _ in range(n)]
arr2 = [list(map(int, input())) for _ in range(n)]

def reverse(arr, y, x):
    for i in range(y, y+3):
        for j in range(x, x+3):
            if arr[i][j] == 0:
                arr[i][j] = 1
            elif arr[i][j] == 1:
                arr[i][j] = 0
    return arr

def same(arr1, arr2):
    flag = 1
    for i in range(n):
        for j in range(m):
            if arr1[i][j] != arr2[i][j]:
                flag = 0
                break
        if flag == 0: break
    return flag

cnt = 0
for i in range(n-2):
    for j in range(m-2):
        if arr1[i][j] != arr2[i][j]:
            reverse(arr1, i, j)
            cnt += 1
            if same(arr1, arr2):
                break
    if same(arr1, arr2):
        break
if same(arr1, arr2) == 0:
    cnt = -1
print(cnt)