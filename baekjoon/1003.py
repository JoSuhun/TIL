T = int(input())
for tc in range(T):
    n = int(input())
    arr = [[1, 0], [0, 1]]+[[0, 0] for _ in range(n-1)]
    for i in range(2, n+1):
        arr[i][0] = arr[i-1][0]+arr[i-2][0]
        arr[i][1] = arr[i-1][1]+arr[i-2][1]
    print(arr[n][0], arr[n][1])