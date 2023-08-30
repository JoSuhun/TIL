T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())    # n 컨테이너 // m 트럭
    nlst = list(map(int, input().split()))
    mlst = list(map(int, input().split()))

    nlst.sort()
    mlst.sort()

    cidx = n-1
    bidx = m-1
    SUM = 0

    while cidx >= 0 and bidx >= 0:
        if nlst[cidx] <= mlst[bidx]:
            SUM += nlst[cidx]
            cidx-=1
            bidx-=1
        else:
            cidx-=1
    print(f'#{tc} {SUM}')
