# 전기버스

T = int(input())

for tc in range(T):

    k, n, m = map(int, input().split())

    chars = list(map(int, input().split()))
    

    flag = 0

    for i in range(1, m):
        if chars[i] - chars[i-1] > k or chars[0]>k or n-chars[-1]>k:
            flag = 1
            
    if flag == 1:
        print(f'#{tc+1} 0')

    else:

        if chars[1] <= k:
            m-=1
        if n-chars[-2] <= k:
            m-=1

        for i in range(0, m-2):
            if chars[i+2] - chars[i] <= k:
                m -= 1
                chars[i+1] = 0
        
        print(f'#{tc+1} {m}')