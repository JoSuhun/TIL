s1 = input()
s2 = input()
len1 = len(s1)
len2 = len(s2)
dp = [[0]*(len1+1) for _ in range(len2+1)]
for i in range(1, len2+1):
    for j in range(1, len1+1):
        if s2[i-1] == s1[j-1]: dp[i][j] = dp[i-1][j-1]+1
        else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(dp[len2][len1])