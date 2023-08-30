T = int(input())
for tc in range(1, T+1):
    n = int(input())
    #
    # time = [0]*24
    # cnt = 0
    # for _ in range(n):
    #     st, ed = map(int, input().split())
    #     flag = 0
    #     backup = time[:]
    #     for i in range(st, ed):
    #
    #         if time[i]+1 == 2:
    #             flag = 0
    #             time = backup[:]
    #             break
    #         time[i] += 1
    #         flag = 1
    #     cnt += flag
    #
    # print(cnt)
    #

    lst = [list(map(int, input().split())) for _ in range(n)]
    print(lst)













