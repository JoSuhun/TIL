n = int(input())    # n개의 국가
people = list(map(int, input().split()))

arr = [0]*200
def findboss(mem):
    global arr
    if arr[ord(mem)] == 0:
        return mem
    ret = findboss(arr[ord(mem)])
    return ret

def union(a, b):
    global arr
    fa, fb = findboss(a), findboss(b)
    if fa == fb:
        return
    arr[ord(fb)] = fa


t = int(input())
t-=1
for _ in range(t):
    x, a, b = map(str, input().split())
    union(a, b)

x, a, b = map(str, input().split())
def find(boss):
    cnt = 0
    total = 0
    for i in range(n):
        t = chr(65+i)
        ret = findboss(t)
        if ret == boss:
            cnt += 1
            total += people[ord(t)-65]
    return cnt, total

acnt, atotal = find(a)
bcnt, btotal = find(b)
if atotal < btotal:
    print(n-acnt)
else:
    print(n-bcnt)