arr = [[3, 2, 5, 3],
       [7, 6, 1, 6],
       [4, 9, 2, 7]]

result = [[0]*4 for _ in range(3)]
msg = list(map(int, input().split()))

def move(now, msg, cnt):
    if cnt == msg:
        return

    arr[0][now], arr[2][now] = arr[2][now], arr[0][now]
    arr[1][now], arr[2][now] = arr[2][now], arr[1][now]
    move(now, msg, cnt+1)

for i in range(4):
    move(i, msg[i], 0)

for a in arr:
    print(*a, sep='')