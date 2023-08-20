from collections import deque


def bfs(now, end):
    q = deque()
    q.append((now, 0))
    used = [0]*v

    while q:
        now, level = q.popleft()
        if now == end: return level

        if used[now] == 1: continue # 양방향이야
        used[now] = 1
        for i in lst[now]:
             q.append((i, level+1))
    return 0

T = int(input())
for tc in range(1, T+1):
    v, e = map(int, input().split())
    lst = [[] for _ in range(v)]
    for _ in range(e):
        st, ed = map(int, input().split())
        lst[st-1].append(ed-1)
        lst[ed-1].append(st-1)

    s, g = map(int, input().split())
    s -=1
    g -=1

    ret = bfs(s, g)
    print(f'#{tc} {ret}')