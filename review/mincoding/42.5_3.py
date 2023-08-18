import copy
n = int(input())
arrs = list(map(int, input().split()))


def cal(sign):
    nums = copy.deepcopy(arrs)
    while True:
        if sign[0] == '!!':
            a = nums.pop(0)
            b = nums.pop(0)
            new = (a-b) * (a+b)
            nums.insert(0, new)
            sign.pop(0)
        elif sign[0] == '#':
            a = nums.pop(0)
            b = nums.pop(0)
            new = max(a, b)
            nums.insert(0, new)
            sign.pop(0)
        elif sign[0] == '$':
            a = nums.pop(0)
            b = nums.pop(0)
            new = a**2 - b**2
            nums.insert(0, new)
            sign.pop(0)
        elif sign[0] == '&':
            a = nums.pop(0)
            b = nums.pop(0)
            new = (a+b)**2
            nums.insert(0, new)
            sign.pop(0)
        if len(sign)==0: break
    return nums[0]


#
m = n-1
path = [' ']*m
arr = ['!!', '#', '$', '&']
cnt = 0
def make(now):
    global cnt

    if now == m:
        ret = path[:]
        if cal(ret) == 100:
            cnt += 1
        return


    for i in range(4):
        path[now] = arr[i]
        make(now+1)


make(0)
print(cnt)
