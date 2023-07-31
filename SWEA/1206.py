for tc in range(100):

    result_lst = []

    N = int(input())
    h_lst = list(map(int, input().split()))

    for i in range(2, N-2):
        left = max(h_lst[i-1], h_lst[i-2])
        right = max(h_lst[i+1], h_lst[i+2])

        max_h = max(left, right)

        if h_lst[i] > max_h:
            result_lst.append(h_lst[i]-max_h)
        else:
            pass

    print(f'#{tc+1} {sum(result_lst)}')
