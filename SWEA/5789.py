T = int(input())
for tc in range(1, T+1):
    box, turn = map(int, input().split())

    lst = [0]*box

    for i in range(1, turn+1):
        st, ed = map(int, input().split())
        for j in range(st-1, ed):
            lst[j] = i
    print(f'#{tc}', *lst)
