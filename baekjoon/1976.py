def findboss(mem):
    global arr
    if arr[mem] == mem:
        return mem
    arr[mem] = findboss(arr[mem])
    return arr[mem]

def union(a, b):
    global arr
    fa, fb = findboss(a), findboss(b)
    if fa == fb:
        return
    arr[fb] = fa

n = int(input())
m = int(input())

arr = [i for i in range(n+1)]
info = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(i, n):
        if info[i][j] == 1:
            union(i+1, j+1)
plan = list(map(int, input().split()))
x = findboss(plan[0])
flag = 1
for i in range(1, m):
    if findboss(plan[i]) != x:
        flag = 0
        break
if flag: print('YES')
else: print('NO')