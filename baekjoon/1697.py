from collections import deque
n, k = map(int, input().split())
MIN = 21e8
used = [0]*100001
def find(now):
    global MIN
    q = deque()
    q.append((now, 0))
    used[now] = 1
    while q:
        now, cnt = q.popleft()
        if now == k:
            MIN = min(cnt, MIN)
        case = [now-1, now+1, now*2]
        for c in case:
            if c < 0: continue
            if c > 100000: continue
            if used[c] == 1: continue
            used[c] = 1
            q.append((c, cnt+1))
    return MIN
find(n)
print(MIN)