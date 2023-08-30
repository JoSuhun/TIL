def dfs(now):
    global MAX
    if now == cnt:
        ret = int(''.join(nums))
        if ret > MAX:
            MAX = ret
        return

    for i in range(len(nums)-1):
        for j in range(i, len(nums)):
            nums[i],nums[j] = nums[j],nums[i]
            dfs(now+1)
            nums[j], nums[i] = nums[i],nums[j]



T = int(input())
for tc in range(1, T+1):
    nums, cnt = map(int, input().split())
    nums = list(str(nums))
    MAX = -1
    dfs(0)
    print(f'#{tc} {MAX}')
