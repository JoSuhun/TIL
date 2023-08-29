n = int(input())
arrs = [list(map(int, input().split())) for _ in range(n)]
bit = [list(map(int, input().split())) for _ in range(n)]

ans = []
for i in range(n):
    for j in range(n):
        if bit[i][j] == 1:
            ans.append(arrs[i][j])
ans = sorted(ans, key=lambda x: (-ans.count(x), x))
print(*ans)