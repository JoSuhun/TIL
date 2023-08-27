n = int(input())
points = [list(map(int, input().split())) for _ in range(n)]
used = [0 for _ in range(n)]
MIN = 21e8

def dfs(start, now):
    global MIN

    if now == n//2:
        my = 0
        against = 0
        for i in range(n):
            for j in range(n):
                if used[i] + used[j] == 2:
                    my += points[i][j]
                if used[i] + used[j] == 0:
                    against += points[i][j]
        MIN = min(MIN, abs(my-against))
        return

    for i in range(start, n):
        if used[i] == 1: continue
        used[i] = 1
        dfs(i+1, now+1)
        used[i] = 0

dfs(0, 0)
print(MIN)
