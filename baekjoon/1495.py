n, s, m = map(int, input().split())
vlst = list(map(int, input().split()))
print(vlst)
dp = [s]+[0]*n
for i in range(n):
    if vlst[i]+dp[i] <= m:
        dp[i+1] = vlst[i]+dp[i]
    else:
        dp[i+1] = dp[i] - vlst[i]
print(dp)