T = int(input())

for tc in range(T):

    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    lst = []

    for i in range(0, n-m+1):
        lst.append(sum(nums[i:i+m]))

    print(f'#{tc+1} {max(lst)-min(lst)}')
