bung = [list('ABCEFG'),list('HIJKLM'), list('NOPQRS')]

msg = list(input())


idx = []
for m in msg:
    for i in range(3):
        for j in range(6):
            if bung[i][j] == m:
                idx.append((i, j))

arrs = [[0]*6 for _ in range(3)]
def check(y, x):
    global arrs
    directy = [0, 0, 1, -1]
    directx = [1, -1, 0, 0]
    arrs[y][x] += 1
    for k in range(4):
        dy = y + directy[k]
        dx = x + directx[k]
        if dy<0 or dx<0 or dy>2 or dx>5: continue
        arrs[dy][dx] += 1

for i in idx:
    y = i[0]
    x = i[1]
    check(y,x)

for i in range(3):
    for j in range(6):
        if arrs[i][j]%2 == 1:
            bung[i][j] = '#'
for b in bung:
    print(*b, sep='')