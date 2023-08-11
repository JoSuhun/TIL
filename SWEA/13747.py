T = int(input())

for tc in range(1, T+1):
    n = int(input())

    arr = list(map(int, input().split()))

    start = n-1
    SUM = 0
    while True:
        for i in range(start, -1, -1):
            if arr[i] > arr[start]:
                break
            else:
                SUM += arr[start]
                SUM -= arr[i]
        start = i
        if start == 0: break

    print(f'#{tc} {SUM}')