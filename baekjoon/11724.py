n, m = map(int, input().split())

arr= [[] for _ in range(n)]
used = [0]*n
for i in range(m):
    s, e = map(int, input().split())
    s -= 1
    e -= 1
    arr[s].append(e)
    arr[e].append(s)
def dfs(now):
    used[now] = 1
    for i in arr[now]:
        if used[i] == 1: continue
        dfs(i)

cnt = 0
for i in range(n):
    if used[i] == 0:
        dfs(i)
        cnt += 1
print(cnt)