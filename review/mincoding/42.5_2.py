arrs = [list(input()) for _ in range(4)]
n = int(input())

names = []
for i in range(4):
    for j in range(4):
        if arrs[i][j] != '_':
            names.append((i,j))


used = [0]*len(names)
path = [' ']*n
result = []
def choice(start, now):
    if now == n:
        result.append(path[:])
        return

    for i in range(start, len(names)):
        if used[i] == 1: continue
        used[i] = 1
        path[now] = names[i]
        choice(i+1, now+1)
        used[i] = 0

choice(0, 0)



def bomb(lst):
    SUM = 0
    visited = [[0]*4 for _ in range(4)]

    directy = [0, 0, 1, -1]
    directx = [1, -1, 0, 0]

    for p in lst:
        y = p[0]
        x = p[1]
        if visited[y][x] == 0:
            visited[y][x] = 1
            SUM += 1
        for i in range(4):
            dy = y + directy[i]
            dx = x + directx[i]
            if dy<0 or dx<0 or dy>3 or dx>3: continue
            if visited[dy][dx] == 1: continue
            if arrs[dy][dx] != '_': SUM +=1
            visited[dy][dx] = 1

    return SUM

MAX = -21e8
for lst in result:
    ret = bomb(lst)
    if ret > MAX:
        MAX = ret
        ans = lst

alpha = []
for a in ans:
    alpha.append(arrs[a[0]][a[1]])

alpha.sort()
print(*alpha)