import sys
input = sys.stdin.readline
n, m = map(int, input().split())    # n 노드 수 // m 간선 수
lst = [[] for _ in range(n)]
for _ in range(m):
    s, e = map(int, input().split())
    s-=1
    e-=1
    lst[e].append(s)


def dfs(now):
    global cnt

    for i in lst[now]:
        if used[i] == 1: continue
        used[i] = 1
        cnt += 1
        dfs(i)
        used[i] = 0

    return cnt

ans = [0]*n
for i in range(n):
    cnt = 0
    used= [0]*n
    used[i] = 1
    dfs(i)
    ans[i] = cnt

MAX = max(ans)
for i in range(n):
    if ans[i] == MAX:
        print(i+1, end=' ')