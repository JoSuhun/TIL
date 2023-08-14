# 인접 리스트
while True:
    try:
        tc, n = map(int, input().split())
        arr = list(map(int, input().split()))

        result = [[ ] for _ in range(100)]

        for i in range(n):
            result[arr[2*i]].append(arr[2*i+1])

        print(result)

        flag = 0
        def dfs(now):
            global flag
            if now == 99:
                flag = 1

            for lst in result[now]:
                dfs(lst)

        dfs(0)

        print(f'#{tc} {flag}')



    except:
        break