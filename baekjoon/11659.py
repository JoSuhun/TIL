import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))

SUM_lst = [0]
SUM = 0
for num in nums:
    SUM += num
    SUM_lst.append(SUM)

for _ in range(M):
    i, j = map(int, input().split())
    print(SUM_lst[j]-SUM_lst[i-1])
