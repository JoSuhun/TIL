T = int(input())

for tc in range(1, T+1):
    arrs = []
    for _ in range(9):
        arrs.append(list(map(int, input().split())))
    
    flag = 1

    # 작은 격자
    def getSum(y,x):
        SUM = 0
        for i in range(3):
            for j in range(3):
                SUM += arrs[3*y+i][3*x+j]
        return SUM


    for i in range(3):
        for j in range(3):
            ret = getSum(i,j)
            if ret != 45:
                flag = 0
                break
        if flag == 0:
            break
                

    # 열
    for i in range(9):
        row_sum = 0
        for j in range(9):
            row_sum += arrs[i][j]
        if row_sum != 45:
            flag = 0
            break
    
    # 행

    for j in range(9):
        col_sum = 0
        for i in range(9):
            col_sum += arrs[i][j]
        if col_sum != 45:
            flag = 0
            break
    
    if flag == 0:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} 1')
