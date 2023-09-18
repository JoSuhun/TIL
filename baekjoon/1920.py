n = int(input())
lst = list(map(int, input().split()))
lst.sort()
m = int(input())
targets = list(map(int, input().split()))

for target in targets:
    st = 0
    ed = n-1
    find = 0
    while st<=ed:
        midx = (st+ed)//2
        mv = lst[midx]
        if target == mv:
            find = 1
            break
        elif target < mv:
            ed = midx-1
        elif target > mv:
            st = midx+1

    if find:
        print(1)
    else:
        print(0)