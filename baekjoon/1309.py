import sys
input = sys.stdin.readline
n = int(input())
# now = 1
# a=2
# b=1
# SUM = 0
# while True:
#     SUM = a+b
#
#     if now == n:
#         print(SUM%9901)
#         break
#     temp = a
#     a = a+b*2
#     b = temp+b
#     now+=1



if n == 1:
    print(3)
else:
    lst = [0] * n
    lst[0] = 3
    lst[1] = 7
    for i in range(2, n):
        lst[i] = (lst[i-1]*2 + lst[i-2])%9901
    print(lst[n-1])