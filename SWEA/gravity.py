T = int(input())
for tc in range(1, T+1):
    N = int(input())
    H_lst = list(map(int, input().split()))

    max_cnt = 0

    for i in range(len(H_lst)-1):
        cnt = 0
        for j in range(i+1, len(H_lst)):
            if H_lst[i] > H_lst[j]:
                cnt += 1
        if cnt > max_cnt:
            max_cnt = cnt

    print(f'#{tc} {max_cnt}')
