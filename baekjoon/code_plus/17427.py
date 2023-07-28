# import sys

# N = int(sys.stdin.readline())

# total = 0

# for i in range(1, N+1):
#     cnt_lst = []
#     for j in range(1, i+1):
#         if i%j==0:
#             cnt_lst.append(j)
#     total += sum(cnt_lst)
# print(total)

# 런런런 런타임오류~~

import sys

N = int(sys.stdin.readline())

total = 0

for i in range(1, N+1):
    total += (N//i) * i

print(total)