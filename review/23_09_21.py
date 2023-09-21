# # [1] LCS (Longest Common Substring)
# s1 = input()
# s2 = input()
#
# def lcs(s1, s2):
#     len1, len2 = len(s1), len(s2)
#
#     arr = [[0]*(len2+1) for _ in range(len1+1)]     # dp 테이블
#
#     MAX = 0
#
#     for i in range(1, len1+1):
#         for j in range(1, len2+1):
#             if s1[i-1] == s2[j-1]:
#                 arr[i][j] = arr[i-1][j-1]+1
#                 MAX = max(MAX, arr[i][j])
#             else:
#                 arr[i][j] = 0
#     return MAX
# print(lcs(s1, s2))

# # [2] LCS (Longest Common Subsequence)
# s1 = input()
# s2 = input()
#
# def lcs(s1, s2):
#     len1, len2 = len(s1), len(s2)
#
#     arr = [[0]*(len2+1) for _ in range(len1+1)]     # dp 테이블
#
#     for i in range(1, len1+1):
#         for j in range(1, len2+1):
#             if s1[i-1] == s2[j-1]:
#                 arr[i][j] = arr[i-1][j-1]+1
#             else:
#                 arr[i][j] = max(arr[i-1][j], arr[i][j-1])
#     return arr[len1][len2]
# print(lcs(s1, s2))

# [3] LIS 촤장 증가 부분 수열

n = int(input())
arr = list(map(int, input().split()))

result = [1] * n

for y in range(n):
    code = arr[y]
    for x in range(n):
        value = arr[x]
        if code > value:
            result[y] = max(result[x]+1, result[y])
print(max(result))