n = int(input())    # n*n 방 크기
arrs = [list(input()) for _ in range(n)]

SUM1 = 0
SUM2 = 0
for i in range(n):
    r_cnt = 0
    c_cnt = 0
    for j in range(n):
        if arrs[i][j] == '.':
            r_cnt += 1
        elif arrs[i][j] == 'X':
            if r_cnt >=2:
                SUM1 += 1
            r_cnt = 0
        if j == n-1:
            if r_cnt >=2: SUM1 += 1

        if arrs[j][i] == '.':
            c_cnt += 1
        elif arrs[j][i] == 'X':
            if c_cnt >=2:
                SUM2 += 1
            c_cnt = 0
        if j == n-1:
            if c_cnt >=2: SUM2 += 1

print(SUM1, SUM2)

