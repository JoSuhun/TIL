# # 1,2,3등 뽑기
#
# n = int(input())
# names = list(range(n))
#
# used = [0] * n
# cnt = 0
# def abc(now):
#     global cnt
#     if now == 3:
#         cnt += 1
#         return
#
#     for i in range(n):
#         if used[i] == 1: continue
#         used[i] = 1
#         abc(now+1)
#         used[i] = 0
#
# abc(0)
# print(cnt)





# # 네모블럭 돌리기
#
# a = [list(map(int, input().split())) for _ in range(3)]
#
# b = [list(map(int, input().split())) for _ in range(3)]
# n_arr = [[0]*3 for _ in range(3)]
# flag = 1
# cnt = 0
#
# def isSame(arr1, arr2):
#     global flag
#
#     for i in range(3):
#         for j in range(3):
#             if arr1[i][j] != arr2[i][j]:
#                 flag = 0
#                 break
#         if flag == 0: break
#
#     return flag
#
#
# def turnarr(arr):
#     global n_arr, cnt
#
#     cnt +=1
#
#     for i in range(3):
#         for j in range(3):
#             n_arr[i][j] = arr[j][2-i]
#
#     if isSame(n_arr, b):
#         return
#     else:
#         turnarr(n_arr)
#
# turnarr(a)
# print(cnt)





# 트리인접행렬

arrs = [list(map(int, input().split())) for _ in range(6)]
names = ['A','B','C','D','E','F']
path = [' ']*6

def dfs(now):
    global path

    if 1 not in arrs[now]:
        path[0] = names[0]
        path[now] = ' '
        print(*path, sep='')
        return

    for i in range(6):
        if arrs[now][i] == 1:
            path[now+1] = names[i]
            dfs(i)


dfs(0)















