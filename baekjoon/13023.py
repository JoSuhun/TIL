n, m = map(int, input().split())
arr = [[] for _ in range(n)]
used = [0]*n

for i in range(m):
    s, e = map(int, input().split())
    arr[s].append(e)
    arr[e].append(s)

ret = 0
def dfs(now, lev):
    global ret
    if lev == 5:
        ret = 1
        return
    used[now] = 1
    for i in arr[now]:
        if used[i] == 1: continue
        used[i] = 1
        dfs(i, lev+1)
    used[now] = 0

for i in range(n):
    used[i] = 1
    dfs(i, 1)
    if ret:
        print(1)
        break
if not ret:
    print(0)