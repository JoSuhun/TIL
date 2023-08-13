# # 인접 리스트로 ,, 경로 최소값 구하기 ( ^ ,. ^ ) ...
#
# name = list('ABCD')
#
# n, m = map(int,input().split())
#
# lst = [[] for _ in range(n)]
#
# for i in range(m):
#     s, e, c = map(int, input().split())     # 시작점, 도착점, 이동 비용
#     lst[s].append((e,c))
#     lst[e].append((s,c))        # 양방향이야
#
#
# used = [0]*n        # 사이클을 조심해
# SUM = 0
# MIN = 21e8
#
# used[0] = 1
# def dfs(now, SUM):
#     global MIN
#
#     if now == 3 and MIN > SUM:
#         MIN = SUM
#         print(MIN)
#
#     for i in lst[now]:
#         if used[i[0]] == 1: continue
#         used[i[0]] = 1
#         dfs(i[0],SUM+i[1])
#         used[i[0]] = 0
#
# dfs(0,0)



# # # 각 층에서 숫자 1개씩 택하여 계단을 내려옵니다.  (********************)
# # # 4개의 층에서 택한 숫자들의 합이 20 이상인 경우는 몇가지 일까요??
# #
# arr=[[4,5,2],
#      [-2,1,6],
#      [3,9,-4],
#      [3,5,2]]
#
#
# SUM = 0
# cnt = 0
# def dfs(now,SUM):
#     global cnt
#
#     if now == 4:
#         if SUM >= 20:
#             cnt+=1
#         return
#
#     for i in range(3):
#         dfs(now+1,SUM+arr[now][i])
#
# dfs(0,0)
# print(cnt)



# # 아무렇게나 내려옴  (**************************)
#
#
# arr = [[3, 5, 9, 6],
#        [7, -8, 1, 6],
#        [-10, 2, 3, 9],
#        [5, 1, 2, 8],
#        [4, 7, 1, 8]]
#
# SUM = 0
# cnt = 0
#
#
# def dfs(y,x,SUM):
#     global cnt
#
#     if y == 4:
#         if SUM>=30:
#             cnt +=1
#         return
#
#     for i in range(3):
#         direct = [-1, 0, 1]
#         dy = y+1
#         dx = x + direct[i]
#         if dx<0 or dx>3: continue
#
#         dfs(dy,dx,SUM+arr[dy][dx])
#
# for i in range(4):
#     dfs(0, i, arr[0][i])
# print(cnt)



# 미로찾기  (*************************************************)

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






















