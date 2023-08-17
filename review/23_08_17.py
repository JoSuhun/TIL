# #bfs 복습이야
#
from collections import deque
# name = ['A','B','C','D','E','F']
# arr = [[0, 0, 1, 1, 0, 0],
#        [1, 0, 1, 0, 0, 1],
#        [1, 0, 0, 1, 1, 0],
#        [0, 0, 0, 0, 1, 1],
#        [0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0]]
#
# q = deque()
# q.append(1)
# used = [0]*6
# used[1] = 1
#
# while q:
#     now = q.popleft()
#     print(name[now], end='')
#     for i in range(6):
#         if arr[now][i] == 1 and used[i] == 0:
#             used[i] = 1
#             q.append(i)






# # # 입력받은 좌표에 꽃이 언제 필까?
#
# yy, xx = map(int, input().split())
#
# arrs = [[0]*4 for _ in range(4)]
#
# arrs[2][1] = 1      # 2, 1에 꽃이 피어있어 하루에 인접한 + 방향으로 꽃이 핌
#
# q = deque()
# q.append((2, 1, 1))
#
# directy = [0, 0, 1, -1]
# directx = [1, -1, 0, 0]
# ans = 0
#
# while q:
#     y, x, level = q.popleft()
#
#     if y == yy and x == xx:
#         ans = level
#
#     for i in range(4):
#         dy = y + directy[i]
#         dx = x + directx[i]
#         if dy<0 or dx<0 or dy>3 or dx>3: continue
#         if arrs[dy][dx] != 0: continue
#         arrs[dy][dx] = arrs[y][x] +1
#         q.append((dy, dx, level+1))
#
#         # if dy == yy and dx == xx:
#         #     ans = level+1
#
# print(ans)
# for arr in arrs:
#     print(*arr)





# # 입력받은 좌표에 꽃이 언제 필까? [2]
#
# n = int(input())
#
# arr = [[0]*n for _ in range(n)]
#
# y1, x1, y2, x2 = map(int, input().split())
#
#
# directy = [0, 0, 1, -1]
# directx = [1, -1, 0 ,0]
# flower = [(y1, x1, 1), (y2, x2, 1)]
#
# def bfs(flower):
#     global arr, n
#     q = deque(flower)
#     arr[y1][x1] = 1
#     arr[y2][x2] = 1
#
#     while q:
#         nowy, nowx, level = q.popleft()
#
#         for i in range(4):
#             dy = nowy + directy[i]
#             dx = nowx + directx[i]
#
#             if dy<0 or dx<0 or dy>n-1 or dx>n-1: continue
#             if arr[dy][dx] != 0: continue
#             arr[dy][dx] = arr[nowy][nowx] + 1
#             q.append((dy, dx, level+1))
#
# bfs(flower)
# for a in arr:
#     print(*a)




# # 치즈먹고 여자친구에게 가는 최소 이동 거리
# from collections import deque
# arr=[[0,0,0,0,0,0],
#      [1,0,0,0,1,0],
#      [1,0,0,0,1,0],
#      [0,0,0,0,0,0]]
# directy=[0,0,-1,1]
# directx=[1,-1,0,0]
#
# answer=0
#
# def bfs(sty,stx,edy,edx):
#     q=deque()
#     q.append([sty,stx,0])
#     used=[[0]*5 for _ in range(4)]
#     used[sty][stx]=1
#     while q:
#         now=q.popleft()
#         yy,xx,level=now
#         if yy==edy and xx==edx:
#             return level
#
#         for i in range(4):
#             dy=directy[i]+yy
#             dx=directx[i]+xx
#
#             if dy<0 or dy>3 or dx<0 or dx>4: continue
#             if used[dy][dx]==1: continue # 중복
#             if arr[dy][dx]==1: continue # 벽X
#             used[dy][dx]=1   # 중복 체크 배열에 1 체크하기
#             q.append([dy,dx,level+1])
#
# answer+=bfs(0,0,3,0)
# answer+=bfs(3,0,3,4)
# print(answer)






# # 섬 크기 구하기
# arr = [[0, 0, 1, 0, 0],
#        [0, 0, 1, 0, 0],
#        [0, 1, 1, 1, 0],
#        [0, 0, 1, 0, 0],
#        [0, 0, 0, 0, 0]]
#
# used = [[0]*5 for _ in range(5)]
# cnt = 0
#
# directy = [0, 0, 1, -1]
# directx = [1, -1, 0, 0]
#
# def bfs(y, x):
#     q = deque()
#     q.append([y, x])
#     size = 1
#     arr[y][x] = 0
#
#
#     while q:
#         y, x = q.popleft()
#
#         for i in range(4):
#             dy = y + directy[i]
#             dx = x + directx[i]
#
#             if dx<0 or dy<0 or dx>4 or dy>4: continue
#             if arr[dy][dx] == 1:
#                 q.append([dy, dx])
#                 arr[dy][dx] = 0
#                 size += 1
#
#     return size
#
#
# for i in range(5):
#     for j in range(5):
#         if arr[i][j] == 1:
#             print(bfs(i, j))






# 섬 개수 구하기 / 가장 큰 섬 크기 구하기 / 가장 작은 섬 크기 구하기
arr = [[0, 0, 1, 0, 0],
       [0, 0, 1, 0, 0],
       [0, 1, 1, 1, 0],
       [1, 0, 1, 0, 0],
       [1, 0, 0, 0, 1]]

directy = [0, 0, 1, -1]
directx = [1, -1, 0, 0]


def bfs(y, x):
    q = deque()
    q.append([y,x])
    cnt = 1
    arr[y][x] = 0

    while q:
        y, x = q.popleft()
        for i in range(4):
            dy = y + directy[i]
            dx = x + directx[i]
            if dx<0 or dy<0 or dx>4 or dy>4: continue
            if arr[dy][dx] == 1:
                q.append([dy,dx])
                arr[dy][dx] = 0
                cnt += 1

    return cnt

cnt = 0
MAX = -21e8
MIN = 21e8
for i in range(5):
    for j in range(5):
        if arr[i][j] == 1:
            ret = bfs(i,j)
            cnt += 1
            if ret > MAX:
                MAX = ret
            if ret < MIN:
                MIN = ret
print(MAX, MIN, cnt)









