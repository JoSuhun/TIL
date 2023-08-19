n = int(input())
nums = list(map(int, input().split()))

used = [0]*n
all = [1]*n
path = [0]*n
result = []
def dfs(now, start, SUM):
    global path

    if used == all:
        result.append((path[:], SUM))
        path = [0] * n
        return

    directx = [0, 1, -1]
    for i in range(start, n):
        if used[i] == 1: continue
        used[i] = 1
        path[now] = nums[i]
        for k in range(3):
            dx = i + directx[k]
            if dx<0 or dx>n-1: continue
            if used[dx] == 1: continue
            used[dx] = 1
        dfs(now+1, start+i, SUM+nums[i])
        used[i] = 0
        used[dx] = 0

dfs(0, 0, 0)

MAX = -21e8
for ret in result:
    if ret[1] > MAX:
        MAX = ret[1]
        target = ret[0]
print(target[0], end='')
for i in range(1, len(target)):
    if target[i] == 0: continue
    print(f'+{target[i]}', end='')
print(f'={MAX}')
