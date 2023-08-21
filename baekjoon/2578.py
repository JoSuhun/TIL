arrs = [list(map(int, input().split())) for _ in range(5)]
bingo = [list(map(int, input().split())) for _ in range(5)]

def isBingo(arrs):
    SUM = 0
    x_flag = 1
    re_x_flag = 1
    for i in range(5):
        cnt = 0
        row_cnt = 0
        if arrs[i][i] != 0:
            x_flag = 0
        if arrs[i][4-i] != 0:
            re_x_flag = 0
        for j in range(5):
            if arrs[i][j] == 0:
                cnt += 1
            if arrs[j][i] == 0:
                row_cnt += 1
        if cnt == 5:
            SUM += 1
        if row_cnt == 5:
            SUM += 1
    b_cnt = SUM + x_flag + re_x_flag
    return b_cnt


def find(num):
    for i in range(5):
        for j in range(5):
            if arrs[i][j] == num:
                arrs[i][j] = 0
    return arrs

cnt = 0
endflag = 1
for i in range(5):
    for j in range(5):
        find(bingo[i][j])
        cnt += 1
        ret = isBingo(arrs)
        if ret >= 3:
            endflag = 0
            break
    if endflag == 0:
        break
print(cnt)




