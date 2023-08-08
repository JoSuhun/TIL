T = int(input())
for tc in range(1, T+1):
    M, N = map(int, input().split())
    arrs = [list(map(int, input().split())) for _ in range(M)]

    def isPattern_r(y):
        cnt = 0
        flag = 0
        for i in range(M-N+1):
            for j in range(N):
                if arrs[y][i+j] != 1:
                    flag = 0
                else:
                    flag +=1
        if flag == N:
            cnt +=1
        return cnt

    total = 0
    for y in range(M):
        ret = isPattern_r(y)
        print(ret)
        total += ret

    print(total)

