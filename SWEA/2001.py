T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())

    arrs = []
    for _ in range(n):
        arrs.append(list(map(int, input().split())))


    def getSum(y,x):
        SUM = 0
        for i in range(m):
            for j in range(m):
                SUM += arrs[y+i][x+j]
        return SUM


    MAX = -21e8

    for i in range(n-m+1):
        for j in range(n-m+1):
            ret = getSum(i,j)
            if ret > MAX:
                MAX = ret

    print(f'#{tc} {MAX}')
