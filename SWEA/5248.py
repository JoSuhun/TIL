T = int(input())

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


for tc in range(1, T+1):
    n, m = map(int, input().split())    # n명 // m 쌍의 union
    order = list(map(int, input().split()))
    arr = [0]*(n+1)

    for i in range(m):
        a = order[i * 2]
        b = order[i * 2 + 1]
        union(a, b)

    result = 0
    for i in range(1, n + 1):
        if arr[i] == 0:
            result += 1
    print(f'#{tc} {result}')
