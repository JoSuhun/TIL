"""
10
1 5 2 1 4 3 4 5 2 1
"""
"""
7
"""

n = int(input())
A = list(map(int, input().split()))
result = [1]*n
B = A[::-1]
resultB = [1]*n

for i in range(n):
    for j in range(n):
        if A[i]>A[j]:
            result[i] = max(result[j]+1, result[i])
for i in range(n):
    for j in range(n):
        if B[i]>B[j]:
            resultB[i] = max(resultB[j]+1, resultB[i])

MAX = -1
for i in range(n):
    ret = result[i]+resultB[n-1-i]
    MAX = max(MAX, ret)
print(MAX-1)