n = int(input())
arrs = [list(map(int, input().split())) for _ in range(n)]

edge = []
for i in range(n):
    for j in range(i, n):
        if arrs[i][j] == 1:
            edge.append((i+1, j+1))

arr = [0]*10
def findboss(a):
    global arr
    if arr[a] == 0:
        return a
    ret = findboss(arr[a])
    return ret

def union(a, b):
    global arr
    fa, fb = findboss(a), findboss(b)
    if fa == fb:
        return 1
    arr[fa] = fb

flag = 0
for i in range(len(edge)):
    a, b = edge[i]
    ret = union(a, b)

    if ret == 1:
        flag = 1
        break
if flag: print('cycle 발견')
else: print('미발견')