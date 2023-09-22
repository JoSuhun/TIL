from collections import deque
T=10

def find(start, cnt):
    global MAX, MAX_node, result
    q = deque()
    q.append((start, 0))
    visit[start] = 1

    while q:
        now, cnt = q.popleft()
        if cnt > MAX:
            MAX = cnt
            MAX_node = now

        elif cnt >= MAX:
            MAX_node = max(MAX_node, now)
        for node in arr[now]:
            if visit[node] == 1: continue
            visit[node] =1
            q.append((node, cnt+1))

    return MAX_node

for tc in range(1, T+1):
    n, start = map(int, input().split())
    lst = list(map(int, input().split()))

    arr = [[] for _ in range(101)]
    while lst:
        a, b = lst.pop(0), lst.pop(0)
        arr[a].append(b)

    visit = [0]*101
    MAX = -21e8
    MAX_node = -1

    ret = find(start, 0)

    print(f'#{tc} {ret}')