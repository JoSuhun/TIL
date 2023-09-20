import heapq

n = int(input())

def make(y, x):
    arr[y][x] = 0

    directy = [0, 0, 1, -1]
    directx = [1, -1, 0, 0]
    for i in range(4):
        dy = y + directy[i]
        dx = x + directx[i]
        if dy<0 or dx<0 or dy>n-1 or dx>n-1: continue
        if arr[dy][dx] == 0: continue
        arr[dy][dx] = 0

arr = []
bombs = []
for i in range(n):
    lst = list(map(int, input().split()))
    arr.append(lst)
    for j in range(n):
        heapq.heappush(bombs,(lst[j], i, j))
MAX = -1
while bombs:
    now, y, x = heapq.heappop(bombs)
    if arr[y][x] != 0:
        if MAX < now:
            MAX = now
        make(y, x)

print(f'{MAX}초')
