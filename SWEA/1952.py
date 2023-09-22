T = int(input())


for tc in range(1, T+1):
    d, m, m3, y = map(int, input().split())
    plan = [0] + list(map(int, input().split()))
    ans = [0]*13

    for i in range(1, 13):

        a = [0]*3
        a[0] = ans[i-1] + plan[i]*d
        a[1] = ans[i-1] + m
        if i >= 3: a[2] = ans[i-3] + m3
        else: a[2] = 300000
        ans[i] = min(a)

    print(f'#{tc} {min(ans[12], y)}')