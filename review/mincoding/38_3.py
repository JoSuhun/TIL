from collections import deque
arrs = [list(map(int, input())) for _ in range(7)]

s = []
o = []
for i in range(7):
    for j in range(7):
        if arrs[i][j] == 1:
            s.append((i,j))
        if arrs[i][j] == 2:
            o.append((i,j))

directy = [0, 0, 1, -1]
directx = [1, -1, 0, 0]
def shirmp(y, x):
    s_flag = 1
    for i in range(4):
        for j in range(1, 3):
            dy = y + directy[i]*j
            dx = x + directx[i]*j
            if dy<0 or dx<0 or dy>6 or dx>6: continue
            if arrs[dy][dx] == 1:
                s_flag = 0
                break
        if s_flag == 0: break
    return s_flag
def squid(y, x):
    o_flag = 1
    for i in range(4):
        for j in range(1, 4):
            dy = y + directy[i]*j
            dx = x + directx[i]*j
            if dy<0 or dx<0 or dy>6 or dx>6: continue
            if arrs[dy][dx] == 2:
                o_flag = 0
                break
        if o_flag == 0: break
    return o_flag

flag = 1
for i in s:
    y = i[0]
    x = i[1]
    ret = shirmp(y,x)
    if ret == 0: flag = 0
    break

for i in o:
    y = i[0]
    x = i[1]
    ret = squid(y,x)
    if ret == 0: flag = 0
    break

if flag == 0:
    print('fail')
else:
    print('pass')