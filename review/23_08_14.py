
from collections import deque

# bfs 너비우선탐색
# name=list(input().split()) # M B I K T S
# arr=[
#     [0,1,1,0,0,0],
#     [0,0,0,1,1,0],
#     [0,0,1,0,0,1],
#     [0,0,0,0,0,0],
#     [0,0,0,0,0,0],
#     [0,0,0,0,0,0]]
#
#
#
# def bfs(now):
#     q=deque()
#     q.append(now)
#     while q:
#         now=q.popleft()
#         print(name[now],end=' ')
#
#         for i in range(6):
#             if arr[now][i]==1:
#                 q.append(i)
#
# bfs(0)   # 0-> 탐색 시작 index




# bfs 경로 출력하기

# name = list('BQKFCM')
# arr = [[0, 1, 1, 1, 0, 0],
#        [0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 1, 1],
#        [0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0]]
# answer = []
#
# def bfs(now):
#     q=deque()
#     q.append(now)
#
#     while q:
#         now = q.popleft()
#         answer.append(name[now])
#
#         for i in range(6):
#             if arr[now][i] == 1:
#                 q.append(i)
#
# bfs(0)
# print(*answer)




# bfs 그래프 탐색
# name = 'ABCD'
# arr = [[0, 1, 1, 0],
#        [0, 0, 1, 1],
#        [0, 1, 0, 1],
#        [0, 0, 0, 0]]
#
# used = [0] * 4
#
# ans = []
# def bfs(start):
#     global ans
#     q = deque()
#     q.append(start)
#
#     while q:
#         now = q.popleft()
#         ans.append(name[now])
#         for i in range(4):
#             if arr[now][i] == 1 and used[i] == 0:
#                 used[i] = 1
#                 q.append(i)
#
#
#
# used[0] = 1
# bfs(0)
# print(*ans)




# a에서 d로 가는 경로 찾기기
# import copy
#
# name = 'ABCD'
# arr = [[0, 1, 1, 0],
#        [0, 0, 1, 1],
#        [0, 1, 0, 1],
#        [0, 0, 0, 0]]
# cnt = 0
#
# def bfs(start):
#     global cnt
#     q= deque()
#     used = [0] *4
#     used[start] = 1
#     q.append((start, used))
#
#     while q:
#         now = q.popleft()
#         if now[0] == 3:
#             cnt+=1
#
#         for i in range(4):
#             if arr[now[0]][i] == 1 and now[1][i] == 0:
#                 used = copy.deepcopy(now[1])
#                 used[i] = 1
#                 q.append((i,used))
#
#
# bfs(0)
# print(cnt)




# # 바이러스 퍼지기
# n = int(input())
# arr = [[0]*n for _ in range(n)]
#
# y, x = map(int, input().split())    # 바이러스 시작 좌표 입력
#
# arr[y][x] = 1
# q = deque()
# q.append([y,x])
#
# while q:
#     now = q.popleft()
#     y, x = now
#
#     directy = [0, 0, 1, -1]
#     directx = [1, -1, 0, 0]
#
#     for i in range(4):
#         dy = y + directy[i]
#         dx = x + directx[i]
#         if dy<0 or dx<0 or dy>=n or dx>=n: continue
#         if arr[dy][dx] != 0: continue
#
#         arr[dy][dx] = arr[y][x]+1
#         q.append([dy,dx])
#
# for i in arr:
#     print(*i)




# 며칠 째에 0, 1에 바이러스 도달해?

# n = int(input())
# arr = [[0]*n for _ in range(n)]
#
# y, x = map(int, input().split())
#
# arr[y][x] = 1
# q = deque()
# q.append([y,x])
#
# while q:
#     now = q.popleft()
#     y, x = now
#     if y == 0 and x == 1:
#         print(f'{arr[y][x]}일차')
#         break
#
#     directy = [0, 0, 1, -1]
#     directx = [1, -1, 0, 0]
#
#     for i in range(4):
#         dy = y + directy[i]
#         dx = x + directx[i]
#
#         if dy<0 or dx<0 or dy>=n or dx>=n: continue
#         if arr[dy][dx]!=0: continue
#
#         arr[dy][dx] = arr[y][x]+1
#
#         q.append([dy, dx])











































