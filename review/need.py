# # [1] n개의 주사위를 던졌을 때 경우의 수
#
# n = int(input())
# path = [0]*n
#
# def isSUM(now):
#     if now == n:
#         for i in range(n):
#             print(path[i], end=' ')
#         print()
#         return
#
#     for i in range(6):
#         path[now] = i+1
#         isSUM(now+1)
#
# isSUM(0)


# [2] 미로찾기  (*************************************************)

# arr = [
#     [0,0,0,0],
#     [1,0,1,0],
#     [1,0,1,0],
#     [0,0,0,0]
# ]
#
# directx=[-1,1,0,0]
# directy=[0,0,-1,1]
# used = [[0]*4 for _ in range(4)]
# flag = 0
#
# def dfs(y, x):
#     global flag
#
#     if y == 3 and x == 3:
#         flag = 1
#         return
#
#     for i in range(4):
#         dy = y+directy[i]
#         dx = x+directx[i]
#         if dy<0 or dx<0 or dy>3 or dx>3:
#             continue
#         if used[dy][dx] == 1: continue
#         if arr[dy][dx] == 1: continue
#
#         used[dy][dx] = 1
#         dfs(dy,dx)
#         if flag == 1: return
#
# dfs(0,0)
# if flag == 0: print('못찾아')
# else: print('찾아')
#

