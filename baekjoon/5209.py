def dfs(now, SUM):
    global MIN
    if SUM > MIN:
        return
    if now == n:
        if SUM < MIN:
            MIN = SUM
            return

    for i in range(n):
        if used[i] == 1: continue
        used[i] = 1
        dfs(now + 1, SUM + arr[now][i])
        used[i] = 0

T = int(input())
for tc in range(1, T+1):
    n = int(input())

    arr = [list(map(int, input().split())) for _ in range(n)]

    MIN = 21e8
    used = [[0]*n for _ in range(n)]

    dfs(0, 0)
    print(f'#{tc} {MIN}')