T = int(input())

def isSUM(now, SUM):
    global MIN

    if SUM > MIN: return

    if now == n:
        if SUM < MIN:
            MIN = SUM
        return

    for i in range(n):
        if used[i] == 1: continue
        used[i] = 1
        isSUM(now + 1, SUM + arr[now][i])
        used[i] = 0


for tc in range(1, T+1):

    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    used = [0]*n
    MIN = 21e8

    isSUM(0,0)
    print(f'#{tc} {MIN}')

