def find(SUM):
    global cnt
    lst = [1, 2, 3]
    if SUM == num:
        cnt += 1
        return
    elif SUM > num:
        return
    for i in range(3):
        find(SUM+lst[i])

T = int(input())
for tc in range(T):
    num = int(input())
    cnt = 0
    find(0)
    print(cnt)