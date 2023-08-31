def dfs(start, now):
    global MAX

    if len(nums) ==1:
        MAX = nums[0]

    if now == cnt:
        ret = int(''.join(nums))
        if ret > MAX:
            MAX = ret
        return

    for i in range(start, len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[j] >= nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
                dfs(i, now+1)
                nums[j], nums[i] = nums[i], nums[j]

    if MAX == -1 and now<cnt:
        nums[-1], nums[-2] = nums[-2], nums[-1]
        dfs(i, now+1)
        nums[-2], nums[-1] = nums[-1], nums[-2]


T = int(input())
for tc in range(1, T+1):
    nums, cnt = input().split()
    nums = list(nums)
    cnt = int(cnt)
    MAX = -1
    dfs(0, 0)
    print(f'#{tc} {MAX}')