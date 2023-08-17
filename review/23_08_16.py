# # 동전교환
# # 거슬러 줄 돈을 입력받으면, 최소한의 동전 개수를 사용해 거슬러주기
#
# # 동전교환 문제
# # 최소동전사용개수
#
# changes=int(input())
# coin=[110, 70, 10]
#
# MIN = 21e8
# def dfs(now, SUM):
#     global  MIN
#     if SUM == 0:
#         if now < MIN:
#             MIN = now
#         return
#     if now == 10:
#         return
#
#     for i in range(3):
#         if SUM<0: continue
#         dfs(now+1, SUM-coin[i])
#
# dfs(0, changes)
# print(MIN)






# # T, K, B, S
# # 놀이기구 탈 조합
# names = ['T', 'K', 'B', 'S']
# path = [' ']*3
# used = [0]*4
#
# def dfs(now, level):
#     if now == 3:
#         for i in range(3):
#             print(path[i], end=' ')
#         print()
#         return
#
#     for i in range(level,4):
#         if used[i] == 1: continue
#         used[i] = 1
#         path[now] = names[i]
#         dfs(now+1, i+1)
#         used[i] = 0
#
# dfs(0,0)






# # 숫자 하나씩 뽑기
# # 첫번째 *1, 두번째 *2, 세번째 *3 . . .
# # 모두 더했을 때 0에 가장 가까운 총합은?
# line1 = [5, 2, 7, -5, -7, 9]
# line2 = [4, -5, -7, 9, -5, 3]
#
# used1 = [0]*6
# used2 = [0]*6
# MIN = 21e8
# ans = 0
#
# def dfs(level, SUM):
#     global MIN, ans
#
#     if level == 12:
#         if MIN > abs(SUM):
#             MIN = abs(SUM)
#             ans = MIN
#         return
#
#     if level%2 == 0:
#         for i in range(6):
#             if used1[i] == 1: continue
#             used1[i] = 1
#             dfs(level+1, SUM+line1[i]*(level+1))
#             used1[i] = 0
#     else:
#         for i in range(6):
#             if used2[i] == 1: continue
#             used2[i] = 1
#             dfs(level+1, SUM+line2[i]*(level+1))
#             used2[i] = 0
#
#
#
# dfs(0,0)
# print(ans)






# # 전투력 차이 최소값 찾기
#
# score=[50,40,99,5,25,6,37]
# total = sum(score)
#
# used = [0]*7
# MIN = 21e8
#
# def dfs(level, start, SUM):
#     global MIN
#
#     against = total - SUM
#     gap = abs(SUM - against)
#     MIN = min(MIN, gap)
#
#     if level == 6:
#         return
#
#     for i in range(start, 7):
#         dfs(level+1, i+1, SUM+score[i])
#
# dfs(0,0,0)
# print(MIN)






# # 미로찾기 도착점 이동 횟수 구하기
#
# arr =[[0, 0, 0, 0, 1],
#       [1, 0, 1, 0, 1],
#       [1, 0, 1, 0, 1],
#       [1, 0, 1, 0, 0],
#       [0, 0, 0, 0, 0]]
#
# yy, xx = map(int, input().split())
# visit = [[0]*5 for _ in range(5)]
# directy = [0, 0, 1, -1]
# directx = [1, -1, 0, 0]
# MIN = 21e8
#
# def miro(y, x, cnt):
#     global MIN
#     if y == yy and x == xx:
#         if cnt < MIN:
#             MIN = cnt
#         return
#
#     for i in range(4):
#         dy = y + directy[i]
#         dx = x + directx[i]
#         if dx<0 or dy<0 or dx>=5 or dy>=5: continue
#         if arr[dy][dx] == 1: continue
#         if visit[dy][dx] == 1: continue
#         visit[dy][dx] = 1
#         miro(dy, dx, cnt+1)
#         visit[dy][dx] = 0
#
# miro(0, 0, 0)
# print(MIN)







# 고난도에요
import copy

arr = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]



def digging(y, x):
    directy = [0, 0, 0, 1, -1]
    directx = [0, 1, -1, 0, 0]
    for i in range(5):
        dy = y + directy[i]
        dx = x + directx[i]
        if dy<0 or dx<0 or dy>2 or dx>2: continue
        arr[dy][dx] = arr[dy][dx] * 7 % 10

def getSum():
    SUM = 0
    for i in range(3):
        for j in range(3):
            SUM += arr[i][j]
    return SUM

MAX = -21e8

def dfs(level):
    global MAX, arr
    backup = copy.deepcopy(arr)     # 배열 복사해두기 . . 밑에서 재귀 실행 시키고 배열 원상복구 해줘야됨

    if level == 3:  # arr 배열의 합을 확인 후 최대값 갱신
        result = getSum()
        MAX = max(result, MAX)
        return

    for i in range(3):
        for j in range(3):
            digging(i, j)   # 땅 개발하는 함수
            dfs(level+1)
            arr = copy.deepcopy(backup)     # arr 배열 원상복구!

dfs(0)
print(MAX)














