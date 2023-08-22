T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input()))
    SUM = arr[0]
    cnt = 0
    for i in range(1, len(arr)):
        if SUM >= i:
            SUM += arr[i]
        elif SUM < i:
            cnt += i - SUM
            SUM = i + arr[i]
    print(f'#{tc} {cnt}')