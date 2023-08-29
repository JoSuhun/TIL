# stack
n = int(input())
arr = list(map(int, input().split()))
stack = []
ans  = [0]*n

for i in range(n):
    while stack and arr[stack[-1]] < arr[i]:
        idx = stack.pop()
        ans[idx] = arr[i]
    stack.append(i)

for stk in stack:
    ans[stk] = -1

print(*ans)