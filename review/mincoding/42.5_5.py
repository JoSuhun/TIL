arr = list(map(int, input().split()))
n = int(input())

path = [0]*3*n

def dfs(now):
    if now == 3*n:
        print(path)
        print(arr)
        return

    for i in range(3):
        if now % 3 == 0:
            if arr[i] == 0: continue
            path[now] = arr[i]
            arr[i] = 0
        dfs(now+1)

    for i in range(1,5):
        if now % 3 == 1:
            if arr[i] == 0: continue
            path[now] = arr[i]
            arr[i] = 0
        dfs(now+1)

    for i in range(3,6):
        if now%3 == 2:
            if arr[i] == 0: continue
            path[now] = arr[i]
            arr[i] = 0
        dfs(now+1)

dfs(0)