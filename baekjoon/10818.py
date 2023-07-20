nums=[int(input()) for i in range(9)]
print(nums)

max_num=0
max_index=0
for n in range(len(nums)):
    if nums[n] > max_num:
        max_num=nums[n]
        max_index=n
print(max_num, max_index)