n, k = map(int, input().split())
dp = [[10001]*(k+1) for _ in range(n+1)]
dp[0][0] = 0
coin = [0]
for _ in range(1, n+1):
    coin.append(int(input()))
coin.sort()

for i in range(1, n+1):
    for j in range(1, k+1):
        mok = j // coin[i]
        if j%coin[i] == 0: dp[i][j] = mok
        else:
            if mok == 0:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-coin[i]]+1)

if dp[n][k] >= 10001:
    print(-1)
else:
    print(dp[n][k])
print(dp)