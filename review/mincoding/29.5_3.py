arr = [list(map(int, input().split())) for _ in range(3)]

def isSame(lst):
    flag = 1
    for i in range(2):
        if lst[i] != lst[i+1]:
            flag = 0

    if flag == 1: return 1
    else: return 0

for a in arr:
    ret = isSame(a)
    if ret == 1:
        print(a[0])
    else: print('x')