from collections import deque
import sys
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

choice = deque([])
def find(start, cnt):
    global MIN, check
    if cnt == m:
        total = 0
        for h in home:
            hy, hx = h
            dist = 21e8
            for i in range(len(chicken)):
                if check[i] == 1:
                    cy, cx = chicken[i]
                    dist = min(dist, abs(hy-cy)+abs(hx-cx))
            total += dist
            if total > MIN: return
        MIN = min(MIN, total)
        return

    for idx in range(start, len(chicken)):
        check[idx] = 1
        find(start+1, cnt+1)
        check[idx] = 0

check = [0]*(len(chicken)+1)
MIN = 21e8
for i in range(len(chicken)):
    find(i, 0)
print(MIN)