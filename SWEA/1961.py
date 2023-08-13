T = int(input())

for tc in range(1,T+1):
    n = int(input())
    arrs = [list(map(str, input().split())) for _ in range(n)]


    arrs1 = list([0]*n for _ in range(n))
    arrs2 = list([0]*n for _ in range(n))
    arrs3 = list([0]*n for _ in range(n))

    def re_arr(a,new_a):
        for i in range(n):
            for j in range(n):
                new_a[i][j] = a[n-1-j][i]
        return new_a

    re_arr(arrs, arrs1)
    re_arr(arrs1, arrs2)
    re_arr(arrs2, arrs3)

    result = list(zip(arrs1,arrs2,arrs3))

    print(f'#{tc}')
    for i in range(n):
        for j in range(3):
            print(''.join(result[i][j]), end = ' ')
        print()