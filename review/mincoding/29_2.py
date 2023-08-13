arr = [
    [0, 0, 1, 0, 1, 1],
    [1, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
]

s, e = map(int, input().split())
s -= 1
e -= 1


used = [0]*6
MIN = 21e8
cnt = 0
flag = 0
def dfs(now, cnt):
    global MIN, flag

    if now == e:
        flag = 1
        if cnt < MIN:
            MIN = cnt
        return

    for i in range(6):
        if arr[now][i] == 1 and used[i] != 1:
            used[i] = 1
            dfs(i, cnt+1)
            used[i] = 0

used[s] = 1
dfs(s, 0)
if flag == 0: print(0)
else: print(MIN)