T = int(input())
for tc in range(1, T+1):
    n = int(input())
    nums = list(input())

    max_lst = [0] * 10

    for i in nums:
        max_lst[int(i)] += 1

    max_cnt = max(max_lst)
    max_num = max_lst.index(max_cnt)

    if max_lst.count(max_cnt) > 1:
        for i in range(10):
            if max_lst[9-i] == max_cnt:
                break
        print(f'#{tc} {9-i} {max_cnt}')
    else:
        print(f'#{tc} {max_num} {max_cnt}')
