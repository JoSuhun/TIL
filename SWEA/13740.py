T = int(input())

for tc in range(1,T+1):

    N, M = map(int, input().split())
    arrs = [list(input()) for _ in range(N)]

    # 회문 판별
    def isStr(st, M):
        mid = M//2
        while True:
            if st[mid] != st[M-mid-1]:
                return 0
            mid -= 1
            if mid < 0: break
        return 1

    for i in range(N):
        for j in range(1+N-M):
            st = []
            for k in range(M):
                st.extend(arrs[i][j+k])
            ret = isStr(st, M)
            if ret: print(f'#{tc}', ''.join(st))

    for i in range(N):
        for j in range(1+N-M):
            st = []
            for k in range(M):
                st.extend(arrs[j+k][i])
            ret = isStr(st, M)
            if ret: print(f'#{tc}', ''.join(st))


