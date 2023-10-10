from collections import deque
a, b = map(int, input().split())
q = deque([4, 7])
# 4, 7
ans = 0
while q:
    x = q.popleft()
    if x <= b:
        if x >= a:
            ans += 1
        q.append(x*10+4)
        q.append(x*10+7)
print(ans)