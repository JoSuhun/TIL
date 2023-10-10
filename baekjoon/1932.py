import sys
input = sys.stdin.readline
n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]

ans = [[0]*n for _ in range(n)]
ans[0][0] = lst[0][0]
for i in range(1, n):
    for j in range(i+1):
        ans[i][j] = max(ans[i-1][j]+lst[i][j], ans[i-1][j-1]+lst[i][j])
print(max(ans[n-1]))