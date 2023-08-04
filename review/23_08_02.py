# # 1. 입력받은 배열에서 +모양으로 더한 합의 최댓값은 무엇

# arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# N = len(arr)

# di = [0, 1, 0, -1]
# dj = [1, 0, -1, 0]

# max_v = 0
# for i in range(N):
#     for j in range(N):
#         # arr[i][j]를 중심으로
#         s = arr[i][j]
#         for k in range(4):
#             ni, nj = i+di[k], j+dj[k]
#             if 0 <= ni < N and 0 <= nj < N:
#                 s += arr[ni][nj]
#         # + 모양 인접 원소를 포함한 합
#         if max_v < s:
#             max_v = s

# print(max_v)






# # 2. +모양이 커졌어! 좌우 각각 중심 포함 길이가 m이야

max_v = 0
m = 2   
for i in range(N):
    for j in range(N):
        # arr[i][j]를 중심으로
        s = arr[i][j]
        for k in range(4):
            for p in range(1, m):       # 늘어난 m길이 만큼 +를 늘여주자!
                ni, nj = i+di[k]*p, j+dj[k]*p
                if 0 <= ni < N and 0 <= nj < N:
                    s += arr[ni][nj]
        # + 모양 인접 원소를 포함한 합
        if max_v < s:
            max_v = s






# # 전치 행렬
# arrs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
# for i in range(3):
#     for j in range(3):
#         if i < j:
#             arrs[i][j], arrs[j][i] = arrs[j][i], arrs[i][j]
#
# print((arrs))
#
# # 교수님과의 ~~ 문제풀이 ~~ 시간 ~~
# #

# target 이라는 리스트에 0~7 사이의 정수 3개 입력받기
# n 이라는 변수에 1~5 사이의 정수를 입력받기

# 입력받은 정수로 부터 연속된 n개의 정수의 합이
# 맥스일때의 정수값과 max값을 출력하시오

# lst = [4,3,5,1,7,5,6,8,1,6,9,5]

# target = list(map(int, input().split()))
# n = int(input())

# MAX = 0
# answer = 0

# # 나의 코드
# MAX = 0
# for t in target:
#     SUM = 0
#     for i in range(n):
#         SUM += lst[t+i]
#     if SUM > MAX:
#         MAX = SUM

# print(MAX)

# # 교수님의 코드! 합을 구해주는 함수
# def getSum(t):
#     SUM = 0
#     for i in range(t, t+n):
#         SUM += lst[i]
#     return SUM

# for i in range(len(target)):
#     ret = getSum(target[i])
#     if ret > MAX:
#         MAX = ret
#         answer = target[i]

# print(answer, MAX)

#
# # # # 연속되는 숫자 3개의 합이 가장 클 때 의 값을 출력해 주세요
# # lst= [[4, 5, 2, 6, 7, 3, 1],
# #       [2, 9, 9, 6, 1, 6, 7]]
# # MAX = 0
# # for i in range(len(lst)):
# #     SUM = 0
# #     for j in range(5):
# #         for k in range(j, j+3):
# #             SUM += lst[i][k]
# #             if MAX < SUM:
# #                 MAX = SUM
# # print(MAX)
#
#
#
# lst= [[4, 5, 2, 6, 7, 3, 1],
#       [2, 9, 9, 6, 1, 6, 7]]
#
# MAX = 0

# def getSUM(y,x):
#     SUM = 0
#     for i in range(3):
#         SUM += lst[y][x+i]
#     return SUM

# for i in range(2):
#     for j in range(5):
#         ret = getSUM(i,j)
#         if ret > MAX:
#             MAX = ret

# print(MAX)

#
# # 1 2 3 4 5
# # 2 4 2 1 3
# # 3 4 5 2 5
# #
# # 3 4 5 라는 패턴이 어느 좌표에 있는지 찾기!!
# #
# # 정답은:
# # 0 2
# # 2 0
#
# arrs = [[1,2,3,4,5],[2,4,2,1,3],[3,4,5,2,5]]
# pattern = [3,4,5]


# for i in range(3):
#     for j in range(3):
#         if arrs[i][j:j+3] == pattern:
#             print(i,j)

# lst=[[1 ,2 ,3 ,4 ,5],
#      [2 ,4 ,2 ,1 ,3],
#      [3 ,4 ,5 ,2 ,5]]

# target=[3, 4, 5]

# def isPattern(y,x):
#     for i in range(3):
#         if target[i]!=lst[y][x+i]:
#             return 0
#     return 1

# for i in range(3):
#     for j in range(3):
#         ret=isPattern(i,j)
#         if ret:
#             print(i,j)

lst=[[1 ,2 ,3 ,4 ,5],
     [2 ,4 ,2 ,1 ,3],
     [3 ,4 ,5 ,2 ,5]]
target = [[3,4],
          [2,1]]

def isPattern(y,x):
    for i in range(2):
        for j in range(2):
            if target[i][j]!=lst[y+i][x+j]:
                return 0
    return 1

for i in range(2):
    for j in range(4):
        ret = isPattern(i,j)
        if ret:
            print(i,j)

#
#
# arrs = [[1,5,4,2],
#         [1,3,4,2],
#         [3,5,3,2],
#         [2,6,4,1]]

# # ***
# # ***

# MAX = 0

# def getSum(y,x):
#     SUM = 0

#     for i in range(2):
#         for j in range(3):
#             SUM += arrs[y+i][x+j]
#     return SUM

# for i in range(3):
#     for j in range(2):
#         ret = getSum(i,j)
#         if ret > MAX:
#             MAX = ret

# print(MAX)
#
#
#
# # a = [8,3,5,2,5,7,2,4]
# #
# # n = int(input())
# # lst = list(map(int, input().split()))
# #
# # for i in lst:
# #     print(f'{i}: {a.count(i)}개 존재')
# #
# # --------------------------------------------------------------
#
# cnt_lst = [0]*10
#
# for i in a:
#     cnt_lst[i] += 1
# print(cnt_lst)
#
# for i in range(len(lst)):
#     print(f'{lst[i]}: {cnt_lst[lst[i]]}개 존재')
#
#
# # --------------------------------------------------------------
#
# for i in range(len(lst)):
#     cnt = 0
#     for j in range(len(a)):
#         if lst[i] == a[j]:
#             cnt+=1
#     print(f'{lst[i]}:{cnt}개 존재')



# --------------------------------------------------------------


# A = [4,7,1,4,2,4,3]

# bucket = [0]*11

# for a in A:
#     bucket[a] += 1

# print(bucket)

# for i in range(len(bucket)-1):
#     bucket[i+1]+=bucket[i]

# print(bucket)

# result = [0]*7

# for i in range(len(A)):
#     bucket[A[i]]-=1
#     index=bucket[A[i]]
#     result[index]=A[i]

# print(result)





