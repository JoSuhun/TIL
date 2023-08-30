n = int(input())
nums = list(map(int, input().split()))
x = int(input())

nums.sort()

st = 0
end = n-1
cnt = 0
while st<end:
    SUM = nums[st]+nums[end]
    if SUM == x:
        st += 1
        cnt += 1
    if SUM > x:
        end -=1
    if SUM < x:
        st += 1
print(cnt)