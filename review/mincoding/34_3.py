n = int(input())
lst = list(input().split())
lst.sort()

m = int(input())
for _ in range(m):
    target, cnt = map(str, input().split())
    cnt = int(cnt)

    st = 0
    ed = n-1
    flag = 0
    c = 0
    while st<= ed:
        md = (st+ed)//2
        c += 1
        if c > cnt: break
        if lst[md] == target:
            flag = 1
            break
        elif lst[md] < target:
            st = md+1
        elif lst[md] > target:
            ed = md-1
    if flag:
        print('pass')
    else:
        print('fail')