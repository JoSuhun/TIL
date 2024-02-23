# 정수 삼각형

triangle = [
    [7], 
    [3, 8], 
    [8, 1, 0], 
    [2, 7, 4, 4], 
    [4, 5, 2, 6, 5]]

def solution(triangle):
    answer = 0

    length = len(triangle)

    dp = [[0]*(length+1) for _ in range(length)]

    dp[0][1] = triangle[0][0]
    for i in range(1, length):
        for j in range(1, i+2):
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j-1]

    answer = max(dp[length-1])
    
    return answer

print(solution(triangle))