m = int(input())
edge = []
for _ in range(m):
    edge.append(input().split())


arr = [0]*200
def findboss(mem):
    global arr
    if arr[ord(mem)] == 0:
        return mem
    else:
        ret = findboss(arr[ord(mem)])
        return ret

def union(a, b):
    global arr
    fa, fb = findboss(a), findboss(b)
    if fa == fb:
        return 1
    else: arr[ord(fa)] = fb

union('A','B')
union('B','C')
union('E','F')
union('F','D')
union('I','J')
union('H','G')
print(arr)
cnt = 4
for i in range(m):
    a, b = edge[i]
    if findboss(a) != findboss(b):
        union(a, b)
        cnt -=1
print(f'{cnt}개')