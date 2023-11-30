import heapq

m, n = map(int, input().split())
miro = [list(map(int, input())) for _ in range(n)]

inf = 21e8
ref = [[inf]*m for _ in range(n)]
ref[0][0] = 0
q = []
def bfs(y, x, cost):
    directy = [0, 0, 1, -1]
    directx = [1, -1, 0, 0]
    heapq.heappush(q, (cost, y, x))
    while q:
        cost, y, x = heapq.heappop(q)
        for i in range(4):
            nowy = y + directy[i]
            nowx = x + directx[i]
            if nowy<0 or nowy>n-1 or nowx<0 or nowx>m-1: continue
            if ref[nowy][nowx] > cost + miro[nowy][nowx]:
                ref[nowy][nowx] = cost + miro[nowy][nowx]
                heapq.heappush(q, (ref[nowy][nowx], nowy, nowx))

bfs(0, 0, 0)
print(ref[n-1][m-1])