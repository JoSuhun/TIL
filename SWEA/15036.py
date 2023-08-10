T = int(input())

for tc in range(1,T+1):

    v, e = map(int, input().split())

    arrs = [[0]*v for _ in range(v)]
    for i in range(e):
        y, x = map(int, input().split())
        arrs[y-1][x-1] = 1

    start, end = map(int, input().split())
    start -= 1
    end -= 1
    flag = 0
    visited = [0]*v
    def dfs(now):
        global start, end,flag

        if now == end:
            flag = 1

        for i in range(v):
            if arrs[now][i] == 1 and visited[i] != 1:
                visited[i] = 1
                dfs(i)
                visited[i] = 0

    dfs(start)
    if flag == 1:
        print(f'#{tc} {flag}')
    else:
        print(f'#{tc} {flag}')