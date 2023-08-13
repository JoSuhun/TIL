n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

path = [0]*3
def dfs(now, level):
    if level == 3:
        for i in range(level):
            print(path[i], end=' ')
        print()
        return

    for i in range(n):
        if arr[now][i] == 1:
            path[level] = i
            dfs(i, level+1)

dfs(0,1)