
for tc in range(1, 11):

    M = int(input())

    arrs = [list(input()) for _ in range(8)]

    # 회문 판별
    def isStr(st, M):
        mid = M// 2
        while True:
            if st[mid] != st[M - mid - 1]:
                return 0
            mid -= 1
            if mid < 0: break
        return 1

    cnt = 0

    for i in range(8):
        for j in range(8-M+1):
            st_r = []
            st_c = []
            for k in range(M):
                st_r.extend(arrs[i][j+k])
                st_c.extend(arrs[j+k][i])

            ret = isStr(st_r, M)
            if ret: cnt += 1

            ret_c = isStr(st_c, M)
            if ret_c: cnt+=1

    print(f'#{tc} {cnt}')
