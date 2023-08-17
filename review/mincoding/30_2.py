arrs = [[0, 0, 1, 0, 2, 0],
        [5, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 7],
        [2, 0, 0, 0, 8, 0],
        [0, 0, 9, 0, 0, 0],
        [4, 0, 0, 7, 0, 0]]

used = [0]*6
SUM = 0

def dfs(y):
    global SUM

    print(y, SUM)

    for i in range(6):
        if arrs[y][i] != 0 and used[i] != 1:
            used[i] = 1
            SUM += arrs[y][i]
            dfs(i)

n = int(input())
used[n] = 1

dfs(n)