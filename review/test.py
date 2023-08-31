m = int(input())
lst = [list(map(int, input().split())) for _ in range(m)]


arr = [0]*200

def findboss(mem):
    global arr
    if arr[mem] == 0:
        return mem
    ret = findboss(arr[mem])
    return ret


def union(a, b):
    global arr
    fa, fb = findboss(a), findboss(b)
    if fa == fb:
        return 1
    else: arr[fa] = fb

edge = []
for i in range(m):
    for j in range(m):
        if lst[i][j] == 1:
            union(i,j)
            edge.append((i,j))


ans = 0
flag = 0
for i in range(m):
    a,b = edge[i]
    ret = union(a, b)
    if ret == 1:
        flag = 1
        break
if flag == 1:
    print('cycle 발견')
else: print('미발견')