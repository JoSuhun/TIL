import sys
def input(): return sys.stdin.readline().rstrip()

def check(y, x, num):
    for i in range(9):
        if sdoku[y][i] == num:
            return False
        if sdoku[i][x] == num:
            return False
    ny = (y//3) * 3
    nx = (x//3) * 3
    for i in range(3):
        for j in range(3):
            if sdoku[i+ny][j+nx] == num:
                return False
    return True


flag = 0

def find(now):
    global flag
    if now >= len(blank):
        flag = 1
        for sdo in sdoku:
            print(''.join(map(str, sdo)))
        return
    if not flag:
        nowy, nowx = blank[now]
        for num in range(1, 10):
            if check(nowy, nowx, num):
                sdoku[nowy][nowx] = num
                find(now+1)
                sdoku[nowy][nowx] = 0


sdoku = [list(map(int, input())) for _ in range(9)]
blank = []
for i in range(9):
    for j in range(9):
        if sdoku[i][j] == 0:
            blank.append((i, j))
find(0)