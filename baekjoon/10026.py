import sys
sys.setrecursionlimit(10**6)
n = int(input())
rgb = [list(input()) for _ in range(n)]
def find(y, x, type, visit):
    directy = [0, 0, 1, -1]
    directx = [1, -1, 0, 0]
    color = []
    if type:
        if rgb[y][x] == 'R' or rgb[y][x] == 'G':
            color.extend(['R', 'G'])
        else:
            color.extend('B')
    else:
        color.extend(rgb[y][x])
    visit[y][x] = 1
    for i in range(4):
        dy = y + directy[i]
        dx = x + directx[i]
        if dy<0 or dy>n-1 or dx<0 or dx>n-1: continue
        if rgb[dy][dx] not in color: continue
        if visit[dy][dx]: continue
        find(dy, dx, type, visit)

cnt = 0
visit = [[0]*n for _ in range(n)]
cnt2 = 0
visit2 = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if not visit[i][j]:
            cnt +=1
            find(i, j, 0, visit)
        if not visit2[i][j]:
            cnt2 += 1
            find(i, j, 1, visit2)
print(cnt, cnt2)
