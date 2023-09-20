n = int(input())

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
    if fa == fb: return 1
    arr[ord(fa)] = fb

union('A','B')
union('B','C')
union('H','G')
union('E','F')
union('F','D')
union('I','J')
print(arr[65:])

cnt = 4
for _ in range(n):
    a, b = map(str, input().split())
    fa, fb = findboss(a), findboss(b)
    if fa != fb:
        union(a, b)
        cnt -=1
print(f'{cnt}개')

































