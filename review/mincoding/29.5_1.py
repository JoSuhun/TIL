s = int(input())
s-=1

arr = [3, 1, 2, 1, 3, 2, 1, 2, 1]

SUM = 0
def run(now):
    global SUM
    if now == len(arr):
        print('도착', end = ' ')
        return

    SUM += arr[now]
    print(arr[now], end=' ')
    run(now+arr[now])
    print(arr[now], end=' ')

print('시작', end=' ')
run(s)
print('시작')