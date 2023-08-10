# # queue
#
# from collections import deque
#
# q = deque()
# q.append(3)
# q.append(4)
# q.append(5)
# q.append(6)
# print(q)
#
# q.popleft()
# print(q)

#
# name = ['Amy', 'Bob', 'Chloe', 'Diane', 'Edger']
# arr = [[0, 1, 0, 1, 0],
#        [0, 0, 0, 1, 0],
#        [0, 1, 0, 1, 0],
#        [0, 0, 0, 0, 1],
#        [1, 0, 0, 0, 0]]
#
# # lst = [0]*5
# #
# # for i in range(5):
# #     for j in range(5):
# #         if arr[i][j] == 1:
# #             lst[j] +=1
# #
# # MAX = -21e8
# # for i in range(5):
# #     if lst[i] > MAX:
# #         MAX = lst[i]
# #
# # print(name[MAX])
#
# SUM = 0
# Max = -1
# MaxIndex = 0
# for j in range(5):
#     SUM = 0
#     for i in range(5):
#         if arr[i][j] == 1:
#             SUM +=1
#     if SUM > Max:
#         Max = SUM
#         MaxIndex = j
# print(name[MaxIndex])

# 형제 있는 노드 찾기 (' ^ ')/

# name = ['A','B','C','D','E','F']
#
# arr=[[0,1,1,0,0,0],
#      [0,0,0,1,1,0],
#      [0,0,0,0,0,1],
#      [0,0,0,0,0,0],
#      [0,0,0,0,0,0],
#      [0,0,0,0,0,0]]
#
# st = input()
# idx = name.index(st)
#
# flag = 1
# for i in range(6):
#     if arr[i][idx] == 1:
#         for j in range(6):
#             if j != idx and arr[i][j] == 1:
#                 flag = 0
#                 print(name[j])
# if flag == 1:
#     print('형제없음')




# DFS (> ㅅ <)/

# tree모양 그래프
# name = ['A','B','C','D','E','F']
#
# arr=[[0,1,1,0,0,0],
#      [0,0,0,1,1,0],
#      [0,0,0,0,0,1],
#      [0,0,0,0,0,0],
#      [0,0,0,0,0,0],
#      [0,0,0,0,0,0]]
#
# def dfs(now):
#     print(name[now],end=' ')
#
#     for i in range(6):
#         if arr[now][i] == 1:
#             dfs(i)
#
# dfs(0)

# name = ['K','B','G','T','M','C']
#
# arr=[[0,0,0,0,0,0],
#      [1,0,1,1,0,0],
#      [0,0,0,0,0,0],
#      [0,0,0,0,1,1],
#      [0,0,0,0,0,0],
#      [0,0,0,0,0,0]]
#
# def dfs(now):
#     print(name[now],end=' ')
#
#     for i in range(6):
#         if arr[now][i] == 1:
#             dfs(i)
#
# dfs(1)


# tree아닌 그래프


# name= ['A','B','C','D']
#
# arr = [[0,1,1,0],
#        [0,0,1,1],
#        [1,1,0,1],
#        [0,0,0,0]]
# used = [0]*4
#
#
# def dfs(now):
#
#     print(name[now],end=' ')
#
#     for i in range(4):
#         if arr[now][i] == 1 and used[i] == 0:
#             used[i] = 1
#             dfs(i)
#
#
# used[0] = 1     # 탐색 시작 인덱스에 해당하는 used배열값 1체크하고 시작
# dfs(0)


# 응용
# name= ['A','B','C','D']
#
# arr = [[0,1,1,0],
#        [0,0,1,1],
#        [0,1,0,1],
#        [0,0,0,0]]
#
# visit = [0]*4
#
# cnt = 0
# def dfs(now):
#     global cnt
#
#     if name[now] == 'D':
#         cnt+=1
#
#     for i in range(4):
#         if arr[now][i] == 1 and visit[i] == 0:
#             visit[i] = 1
#             dfs(i)
#             visit[i] = 0
#
#
# visit[0] = 1
# dfs(0)
# print(cnt)


# 응용 - 최소비용 구하기 !!!!('O')!!!!
# name= ['A','B','C','D']
#
# arr = [[0,4,8,0],
#        [0,0,1,7],
#        [0,1,0,3],
#        [0,0,0,0]]
#
# used = [0]*4
# Min = 21e8
#
# def dfs(now,SUM):
#
#     global Min
#
#     if now == 3:
#         if SUM < Min:
#             Min = SUM
#
#     for i in range(4):
#         if arr[now][i] != 0 and used[i] == 0:
#             used[i] = 1
#             dfs(i,SUM+arr[now][i])
#             used[i] = 0
#
#
# used[0] = 1
# dfs(0,0)        # 탐색 시작 인덱스0, 초기값 SUM = 0
# print(Min)



# 인접 리스트 방식으로 그래프 그리기 . . .
name= list('ABCDEF')

n,m = map(int, input().split())
lst = [[] for _ in range(n)]
for i in range(m):
    s, e = map(int,input().split())
    lst[s].append(e)
# 입력값임
# 6 5
# 0 1
# 0 2
# 1 3
# 1 4
# 2 5

def dfs(now):

    print(name[now], end=' ')

    for i in lst[now]:
        dfs(i)

dfs(0)





















