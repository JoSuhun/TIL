from collections import deque
n, m = map(int, input().split())
lst = list(range(1, n+1))
ans = deque()
st = 0
while len(ans)<=m:
    ans = deque(lst[st])
    for i in range(st+1, st+m):
        ans.append()