arr = [list(input()) for _ in range(4)]

def move(now):

    if now == 5:
        return

    Mst = ['A', 'C', 'D']
    for m in Mst:
        for i in range(4):
            for j in range(3):
                if arr[i][j] == m:
                    y, x = i, j

        directy = [0, 1, 0, -1, 0]
        directx = [1, 0, -1, 0, 1]

        dy = y + directy[now]
        dx = x + directx[now]
        if dy<0 or dy>3 or dx<0 or dx>2: continue
        if arr[dy][dx] != '_': continue
        arr[y][x], arr[dy][dx] = arr[dy][dx], arr[y][x]

    move(now+1)

move(0)
for a in arr:
    print(*a, sep='')

