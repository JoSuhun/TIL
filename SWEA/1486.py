def make(start, SUM):
    global MIN
    if SUM >= top:
        if SUM < MIN:
            MIN = SUM
            return
    for i in range(start, n):
        if used[i] == 1: continue
        used[i] = 1
        make(i, SUM+hs[i])
        used[i] = 0

T = int(input())
for tc in range(1, T+1):
    n, top = map(int, input().split())
    hs = list(map(int, input().split()))
    used = [0]*n
    MIN = 21e8
    make(0, 0)
    print(f'#{tc} {MIN-top}')