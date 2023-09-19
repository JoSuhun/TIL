T = int(input())
for tc in range(1, T+1):
    lst = list(map(int, input().split()))
    n = lst.pop(0)

    cnt = 0
    now = 0
    end = lst[now]+now

    while True:
        if end >= n-1: break
        cnt += 1
        MAX = 0
        for i in range(now+1, end+1):
            if i+lst[i] >= MAX:
                MAX = i+lst[i]
                max_idx = i
        now = max_idx
        end = now + lst[now]

    print(f'#{tc} {cnt}')