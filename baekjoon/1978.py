n = int(input())
nums = list(map(int, input().split()))

nums.sort()

num = nums[-1]
check = [0]*(num+1)
end = int(num**0.5) +1

for i in range(2, end+1):
    if check[i] == 1: continue
    for j in range(i+i, num+1, i):
        check[j] = 1

cnt = 0
flag = 0
for k in range(n):
    if check[nums[k]] == 0 and nums[k]!=1:
        cnt+=1

print(cnt)