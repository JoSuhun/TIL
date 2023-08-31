T = int(input())
for tc in range(1, T+1):
    n = int(input())

    time = [0]*24
    cnt = 0
    lst = [list(map(int, input().split())) for _ in range(n)]
    lst = sorted(lst, key=lambda x: x[1]-x[0])
    for i in range(n):
        st = lst[i][0]
        ed = lst[i][1]
        flag = 0
        backup = time[:]
        for i in range(st, ed):
            if time[i]+1 == 2:
                flag = 0
                time = backup[:]
                break
            time[i] += 1
            flag = 1
        cnt += flag

    print(f'#{tc} {cnt}')












