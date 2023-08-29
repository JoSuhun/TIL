n = int(input())
lst = [list(map(str, input().split())) for _ in range(n)]
ans = [' ']*n

for i in range(n):
    ans[i] = lst[i]
    for j in range(i, 0, -1):
        if int(ans[j][1]) >= int(ans[j-1][1]):
            ans[j], ans[j-1] = ans[j-1], ans[j]

        else: break

    for i in range(3):
        print(ans[i][0], end=' ')
    print()