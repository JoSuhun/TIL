T = int(input())

<<<<<<< HEAD
for tc in range(1,T+1):
    N = int(input())
    nums = list(map(int, input().split()))

    for i in range(N-1):
        for j in range(i, N):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    
    new_nums = [0]*10

    for j in range(10):
        if j%2 == 0:
            new_nums[j] = nums[N-1-(j//2)]
        else:
            new_nums[j]  = nums[(j-1)//2]
    
    print(f'#{tc}',*new_nums)

=======
for tc in range(T):

    N = int(input())
    nums = list(map(int, input().split()))

    new_nums = []

    
>>>>>>> 82c4633c19b810c280f46bf68cae1a4cd2ac9c7a
