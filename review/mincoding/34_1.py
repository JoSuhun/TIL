lst = [4, 4, 5, 7, 8, 10, 20, 22, 23, 24]
target = int(input())
st = 0
ed = len(lst)-1

flag = 0
while st <= ed:
    md = (st+ed)//2
    if lst[md] == target:
        flag = 1
        break
    elif lst[md] > target:
        ed = md-1
    elif lst[md] < target:
        st = md+1

if flag: print('O')
else: print('X')