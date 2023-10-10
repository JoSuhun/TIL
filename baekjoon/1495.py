import sys
input = sys.stdin.readline
n, s, m = map(int, input().split())
# n 곡 개수 // s 시작 볼륨 // m 최대값
vlst = list(map(int, input().split()))
dp = [[0]*(m+1) for _ in range(n+1)]
dp[0][s] = 1

for i in range(1, n+1):
    for j in range(m+1):
        if dp[i-1][j] == 1:
            num1 = j + vlst[i-1]
            num2 = j - vlst[i-1]
            if 0<= num1 <=m:
                dp[i][num1] = 1
            if 0<= num2 <=m:
                dp[i][num2] = 1
ans = -1
for x in range(m, -1, -1):
    if dp[n][x] == 1:
        ans = x
        break
print(ans)