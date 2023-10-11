import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())    # n*n 도시 // 치킨집 최대 m개
mapp = [list(map(int, input().split())) for _ in range(n)]

home = []
chicken = []
for i in range(n):
    for j in range(n):
        if mapp[i][j] == 1:
            home.append((i, j))
        if mapp[i][j] == 2:
            chicken.append((i, j))

def find(start, cnt):
    global MIN, check
    if start > len(chicken): return
    if cnt == m:
        total = 0
        for h in home:
            hy, hx = h
            dist = 21e8
            for i in value:
                cy, cx = chicken[i]
                dist = min(dist, abs(hy-cy)+abs(hx-cx))
            total += dist
            if total > MIN: return
        MIN = min(MIN, total)
        return

    value.append(start)
    find(start+1, cnt+1)
    value.pop()
    find(start+1, cnt)


MIN = 21e8
value = deque()
find(0,0)
print(MIN)