T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())    # 깃발 크기 세로n * 가로m
    flag = [list(input()) for _ in range(n)]

    W = []
    B = []
    R = []
    for i in range(n):
        W.append(flag[i].count('B') + flag[i].count('R'))
        B.append(flag[i].count('W') + flag[i].count('R'))
        R.append(flag[i].count('W') + flag[i].count('B'))

    lst = []
    for w in range(n-2):
        for b in range(w+1, n-1):
            ret = 0
            ret += sum(W[:w+1])
            ret += sum(B[w+1:b+1])
            ret += sum(R[b+1:])
            lst.append(ret)

    print(f'#{tc} {min(lst)}')

