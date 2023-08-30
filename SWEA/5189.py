T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arrs = [list(map(int, input().split())) for _ in range(n)]

    used = [0]*n
    used[0]= 1
    lst = []
    def dfs(now, SUM, cnt):
        global MIN
        if cnt == n:
            SUM += arrs[now][0]
            lst.append(SUM)
            SUM -= arrs[now][0]
            return

        for i in range(1, n):
            if i == now: continue
            if used[i] == 1: continue
            used[i] = 1
            dfs(i, SUM+arrs[now][i], cnt+1)
            used[i] = 0


    dfs(0,0,1)
    print(f'#{tc} {min(lst)}')
