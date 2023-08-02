T = int(input())

for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))

    for i in range(N-1):
        for j in range(i+1, N):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    
    print(f'#{tc}',*nums)

