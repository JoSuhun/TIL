# 최대공약수, 최소공배수, 소수, sliding window, tow pointer
#
# # 최대공약수 GCD
# a, b = map(int, input().split())
#
# # for i in range(2, min(a, b)):
# #     if a%i == 0 and b%i == 0:
# #         ans = i
# # print(ans)
#
#
# # 최대공약수 유클리드호제법
# while b>0:
#     a, b = b, a%b
# print(a)


# # 소수 구하기
# n = int(input())
# # ans = []
# # for i in range(2, n):
# #     flag = 0
# #     for j in range(2, i):
# #         if i%j == 0:
# #             flag = 1
# #             break
# #     if flag == 0: ans.append(i)
# # print(ans)
#
# import math
# end = int(math.sqrt(n))
# check = [0] * (n+1)
#
# for i in range(2, end+1):
#     if check[i] == 1: continue
#     for j in range(i+i, n+1, i):
#         check[j] = 1
#
# for i in range(2, n+1):
#     if check[i] == 0: print(i, end=' ')



# sliding window 연속되는 구간 합
#
# n, m = map(int, input().split())
# # n 개의 정수에서 m 크기의 연속 구간 합 중 가장 큰 값?
#
# arr= list(map(int, input().split()))
#
# SUM = 0
# for i in range(m):
#     SUM += arr[i]
#
# MAX = SUM
#
# for i in range(n-m):
#     SUM += arr[i+m]
#     SUM -= arr[i]
#     if SUM > MAX:
#         MAX = SUM
# print(MAX)




# 투포인터
n, target = map(int, input().split())
nums = list(map(int, input().split()))

start = 0
end = 0
cnt = 0
SUM = 0

while 1:
    if SUM < target:
        SUM += nums[end]
        end += 1
    elif SUM >= target or end == n:
        SUM -= nums[start]
        start += 1
    if SUM == target:
        cnt += 1
    if start == n:
        break

print(cnt)











