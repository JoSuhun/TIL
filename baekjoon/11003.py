from collections import deque
n, l = map(int, input().split())
nums = list(map(int, input().split()))

q = deque()

for i in range(n):
    while q and q[-1][0] > nums[i]:
        q.pop()
    q.append((nums[i], i))
    if i - q[0][1] > l-1:
        q.popleft()
    print(q[0][0], end=' ')