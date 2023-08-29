from collections import deque
s = int(input())
d = int(input())

used = [0]*4
q = deque()
MIN = 21e8
visit = [0]*100001
def bfs(now, s, d):
    global MIN
    q.append((now,s))
    while q:
        now, x = q.popleft()
        if x == d:
            MIN = min(MIN, now)
        if 0<=x//2<=100000 and visit[x//2] ==0:
            visit[x//2] = 1
            q.append((now+1, x//2))
        if 0<=x*2<=100000 and visit[x*2] == 0:
            visit[x*2] = 1
            q.append((now+1, x*2))
        if 0 <= x+1 <= 100000 and visit[x+1] == 0:
            visit[x+1] = 1
            q.append((now+1, x+1))
        if 0 <= x-1 <= 100000 and visit[x-1] == 0:
            visit[x-1] = 1
            q.append((now+1, x-1))


bfs(0, s, d)
print(MIN)