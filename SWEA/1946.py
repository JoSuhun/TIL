T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = []
    for _ in range(N):
        alpha, num = map(str, input().split())
        arr.extend(alpha * int(num))

    print(f'#{tc}')
    x = 0
    while True:

        for i in range(10):
            idx = i + (x*10)
            if idx >= len(arr):
                break
            else:
                print(arr[idx], end='')
        print()
        x += 1
        if 10*x > len(arr): break