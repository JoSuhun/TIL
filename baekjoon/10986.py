import sys
input = sys.stdin.readline
n, m = map(int, input().split())
nums = list(map(int, input().split()))
idx = [0]*m
ans = 0

for i in range(1, n):
    nums[i] += nums[i-1]
for i in range(n):
    nums[i] = nums[i]%m

for num in nums:
    if num == 0: ans += 1
    idx[num]+=1

for i in range(m):
    if idx[i]>1:
        ans += idx[i]*(idx[i]-1)//2
print(ans)