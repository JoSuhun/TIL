# 전기버스 ㅠㅠ

T = int(input())

for tc in range(T):
    k, n, m = map(int, input().split())
    stops = list(map(int, input().split()))
    stops = [0] + stops + [n]

    flag = 0

    for i in range(m+1):
        if stops[i+1] - stops[i] > k:
            flag = 1

    if flag == 1:
        print(f'#{tc+1} 0')

    else:
        i = 1
        step = 0
        cnt = 0
        for i in range(m+1):
            if stops[i] - step > k:
                step = stops[i-1]
                cnt += 1
        if n - step > k:
            cnt += 1

        print(f'#{tc+1} {cnt}')
