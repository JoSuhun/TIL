
# 약수 구하기
n = int(input())

start = 0
end = n-1
arr = list(range(1, n+1))
lst = []

while start <= end:
    if arr[start] * arr[end] == n:
        lst.append(arr[start])
        lst.append(arr[end])
        start+=1
        end-=1
    elif arr[start] * arr[end] < n:
        start +=1
    elif arr[start] * arr[end] > n:
        end -=1

print(lst)


# # 소수구하기 (에라토스테네스의 체)
#
# import math
#
# n = 9
# arr = [True for _ in range(n+1)]
#
# for i in range(2, int(math.sqrt(n))+1):
#     if arr[i] == True:
#         j = 2
#         while i*j <= n:
#             arr[i*j] = False
#             j += 1
#
# for i in range(2, n+1):
#     if arr[i]:
#         print(i, end= ' ')


