import sys
input = sys.stdin.readline
def findboss(mem):
    global arr
    if arr[mem] == mem:
        return mem
    ret = findboss(arr[mem])
    arr[mem] = ret
    return ret

def union(a, b):
    global arr
    fa, fb = findboss(a), findboss(b)
    if fa == fb:
        return
    arr[fb] = fa
def checkunion(a, b):
    fa, fb = findboss(a), findboss(b)
    if fa == fb:
        return 1
    else: return 0

n, m = map(int, input().split())
arr = [i for i in range(n+1)]
for _ in range(m):
    type, a, b = map(int, input().split())
    if type == 1:
        ret = checkunion(a, b)
        if ret: print('YES')
        else: print('NO')
    else: union(a, b)
