n = int(input())
nums = list(range(1, 51))
st = 0
ed = 50
try:
    for _ in range(n):
        num, msg = map(str, input().split())
        num = int(num)
        if msg == 'DOWN':
            ed = nums.index(num)
            nums = nums[:ed]
        else:
            st = nums.index(num)+1
            nums= nums[st:]

    if len(nums) == 1:
        print(*nums)
    else:
        print(f'{nums[0]} ~ {nums[-1]}')
except:
    print('ERROR')