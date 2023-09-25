n = int(input())

inf = 10**8
ans = [inf]*3
# if n%3 == 0: ans[0] = n//3
# if n%2 == 0: ans[1] = n//2
# ans[2] = n-1
#
# cnt = 1
# while True:
#     if n == 1:
#         cnt= 0
#         break
#     if min(ans) == 1: break
#     cnt += 1
#     a = [inf] * 3
#     for i in range(3):
#         if ans[i] == inf: continue
#         if ans[i]%3 == 0:
#             a[0] = min(ans[i]//3, a[0])
#         if ans[i]%2 == 0:
#             a[1] = min(ans[i]//2, a[1])
#         if ans[i]-1 > 0:
#             a[2] = min(ans[i]-1, a[2])
#         if min(a) == 1: break
#     ans = a
#
# print(cnt)

