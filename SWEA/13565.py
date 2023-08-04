# 전기버스 ㅠㅠ

# 전기버스

T = int(input())

for tc in range(T):
    k, n, m = map(int, input().split())
<<<<<<< HEAD
    stops = list(map(int, input().split()))
    stops = [0] + stops + [n]

    flag = 0

    for i in range(m+1):
        if stops[i+1] - stops[i] > k:
            flag = 1

=======

    chars = list(map(int, input().split()))
    

    flag = 0

    for i in range(1, m):
        if chars[i] - chars[i-1] > k:
            flag = 1
    if chars[0] > k or chars[-1] < n - k:
            flag = 1
            
>>>>>>> 82c4633c19b810c280f46bf68cae1a4cd2ac9c7a
    if flag == 1:
        print(f'#{tc+1} 0')

    else:
<<<<<<< HEAD
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
=======

        if chars[1] <= k:
            m-=1
        if chars[-2] >= n - k:
            m-=1

        for i in range(0, m-2):
            if chars[i+2] - chars[i] <= k:
                m -= 1
                chars[i+1] = 0
        
        print(f'#{tc+1} {m}')
>>>>>>> 82c4633c19b810c280f46bf68cae1a4cd2ac9c7a
