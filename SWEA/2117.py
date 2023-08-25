# 운영비용  k*k + (k-1)*(k-1)
# 손해를 보지 않으면서 가장 많이 서비스를 받는 집 개수
from collections import deque


T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())    # n 도시 크기 // m 지불 가능 비용
    arrs = [list(map(int, input().split())) for _ in range(n)]

    def check(y, x):
        q = deque
        q.append((y, x))
        cnt = 0

        visit = [[0] * n for _ in range(n)]
        while q:
            nowy, nowx = q.popleft()
            directy = [0, 0, 1, -1]
            directx = [1, -1, 0, 0]

            for i in range(4):
                dy = nowy + directy[i]
                dx = nowx + directx[i]
                if dy<0 or dx<0 or dy>n-1 or dx>n-1: continue
                if visit[dy][dx] == 1: continue
                visit[dy][dx] = 1
                q.append((dy, dx))
