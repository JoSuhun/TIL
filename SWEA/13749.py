T = int(input())
for tc in range(1, T+1):
    M, N = map(int, input().split())
    arrs = [list(map(int, input().split())) for _ in range(M)]

    total = 0
    for i in range(M):
        cnt = 0
        for j in range(M):
            if arrs[i][j] == 1:
                cnt +=1
            if arrs[i][j] == 0 or j == M-1:
                if cnt == N:
                    total += 1
                cnt = 0

    for j in range(M):
        cnt = 0
        for i in range(M):
            if arrs[i][j] == 1:
                cnt +=1
            if arrs[i][j] == 0 or i == M-1:
                if cnt == N:
                    total += 1
                cnt = 0

    print(f'#{tc} {total}')