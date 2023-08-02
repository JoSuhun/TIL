# 구간의 합 먼저..
N, M = map(int, input().split())
nums = list(map(int, input().split()))

SUM_lst = [0]
SUM = 0
for num in nums:
    SUM += num
    SUM_lst.append(SUM)

cnt = 0
for i in range(len(SUM_lst)-1, 0, -1):
    for j in range(i-1, -1, -1):
        if (SUM_lst[i]-SUM_lst[j]) % M == 0:
            cnt += 1
print(cnt)
