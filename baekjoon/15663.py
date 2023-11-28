n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
visited = [0] * n
temp = []

def dfs(now):
    if now == m:
        print(*temp)
        return
    used = 0
    for i in range(n):
        if not visited[i] and used != nums[i]:
            visited[i] = 1
            temp.append(nums[i])
            used = nums[i]
            dfs(now+1)
            visited[i] = False
            temp.pop()
dfs(0)