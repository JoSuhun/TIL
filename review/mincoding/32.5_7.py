# 4*8
arrs = [list(map(int, input().split())) for _ in range(4)]


lst = []

for i in range(4):
    SUM = 0
    st = 0
    ed = 8
    for j in range(8):
        if arrs[i][j] != 0:
            st = j
            break
    for k in range(st,8):
        if arrs[i][k] == 0:
            ed = k
            break
    for y in range(i,4):
        for x in range(st,ed):
            if arrs[y][x] == 0: break
            SUM +=arrs[y][x]

    lst.append(SUM)
print(max(lst))
