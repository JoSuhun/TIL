for T in range(10):
    tc = int(input())
    arrs = [list(map(int, input().split())) for _ in range(100)]

    sum_lst = []

    r_sum = 0
    for i in range(100):
        r_sum += arrs[i][i]
    sum_lst.append(r_sum)
    
    l_sum = 0
    for i in range(100):
        l_sum += arrs[i][99-i]
    sum_lst.append(l_sum)
    
    for i in range(100):
        sum_lst.append(sum(arrs[i]))
    
    
    for j in range(100):
        col_sum = 0
        for i in range(100):
            col_sum += arrs[i][j]
        sum_lst.append(col_sum)

    print(f'#{T+1} {max(sum_lst)}')
