def isSUM(num):
    if '+' in num:
        nums = list(map(int, num.split('+')))
        return sum(nums)
    else:
        return int(num)

strr = input()
strrr = list(strr.split('-'))
ret = isSUM(strrr[0])
for i in range(1, len(strrr)):
    ret -= isSUM(strrr[i])
print(ret)