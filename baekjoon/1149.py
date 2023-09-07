n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

MIN = 21e8

for i in range(3):
    SUM = arr[0][i]
    now = 1
    while now<n:
        MIN = 21e8
        for j in range(3):
            if