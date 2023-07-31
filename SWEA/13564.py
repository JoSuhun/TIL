T = int(input())
for tc in range(T):
    N = int(input())
    nums = list(map(int, input().split()))
    print(f'#{tc+1} {max(nums)-min(nums)}')
