# 전기버스 ㅠㅠ

# 전기버스

T = int(input())

for tc in range(T):

    k, n, m = map(int, input().split())

    stops = list(map(int, input().split()))

    flag = 0

    for i in range(1, m):
        if stops[i] - stops[i-1] > k:
            flag = 1
    
    if stops[1] > k or stops[-1] < n-k:
        flag = 1


    if flag == 1:
        print(f'#{tc+1} 0')

### 미완이야