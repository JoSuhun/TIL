import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
T = int(input())

def dfs(now):
    global checkT
    visit[now] = 1
    for next in lst[now]:
        if visit[next] == 0:
            checkT[next] = (checkT[now]+1)%2
            dfs(next)
        elif checkT[next] == checkT[now]:
            return 1


for tc in range(1, T+1):
    v, e = map(int, input().split())

    lst = [[] for _ in range(v+1)]
    for _ in range(e):
        s, e = map(int, input().split())
        lst[s].append(e)
        lst[e].append(s)

    visit = [0]*(v+1)
    checkT = [0]*(v+1)
    flag = 1
    for i in range(1, v+1):
        ret = dfs(i)
        if ret:
            flag = 0
            break
    if flag:
        print('YES')
    else: print('NO')