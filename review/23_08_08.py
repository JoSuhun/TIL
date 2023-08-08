# def kmp(t,p):
#     N = len(t)
#     M = len(p)
#     lps = [0] * (M+1)
#
#     j = 0
#     lps[0] = -1
#     for i in range(1,M):
#         lps[i] = j
#         if p[i] == p[j]:
#             j += 1
#         else:
#             j = 0
#     lps[M] = j
#     print(lps)


# 누적합

# arr = [3, 4, 5, 1, 6, 9]
#
# # SUM 매개변수
#
# def abc(level, SUM):
#
#     if level == 5:
#         print(SUM, end = ' ')
#         return
#     abc(level+1, SUM + arr[level+1])
#     print(SUM, end = ' ')
#
# abc(0, arr[0])

# # SUM 전역변수
#
# SUM = arr[0]
#
# def abc(level):
#     global SUM
#
#     if level == 5:
#         print(SUM, end=' ')
#         return
#     SUM += arr[level+1]
#     abc(level+1)
#     SUM -= arr[level+1]
#     print(SUM, end = ' ')
#
# abc(0)
#


# 3, 7, 1, 2 의 카드를 세장씩 뽑았을 때 합이 10이 되는 경우의 수
# br 4 lv 3
# 바닥에서 SUM이 10이면 cnt+=1

# # 지역변수
# card = [3, 7, 1, 2]
# cnt = 0
#
# def abc(level, SUM):
#     global cnt
#
#     if level == 3:
#         if SUM == 10:
#             cnt += 1
#         return
#
#     for i in range(4):
#         abc(level+1, SUM + card[i])
#
# abc(0,0)
# print(cnt)



# # 전역변수
# card = [3, 7, 1, 2]
# cnt = 0
# SUM = 0
#
# def abc(level):
#     global SUM, cnt
#     if level == 10:
#         if SUM == 10: cnt += 1
#         return
#
#     for i in range(4):
#         SUM += card[i]
#         abc(level+1)
#         SUM -= card[i]
#
# abc(0)
# print(cnt)

# # 3,4,1,7,6이 섞여있는 n의 카드 묶음. 합이 10 이하로 나오는 경우?
# # br 5, lv n
# # n 바닥에서 sum이 10 이하면 cnt+=1
#
# arr = [3, 4, 1, 7, 6]
# cnt = 0
#
# n = int(input())
#
# def abc(level, SUM):
#     global cnt, n
#
#     if cnt>10: return
#
#     if level == n:
#         if SUM <= 10:
#             cnt += 1
#         return
#
#     for i in range(5):
#         abc(level+1, SUM+arr[i])
#
#
#
# abc(0,0)
# print(cnt)


# # 4개의 카드 중 3장 뽑기 경우
# arr = ['A', 'B', 'C', 'D']
# path = [' ']*3
#
# def abc(level):
#     if level == 3:
#         for i in range(level):
#             print(path[i], end='')
#         print()
#         return
#
#     for i in range(4):
#         path[level] = arr[i]
#         abc(level+1)
#
# abc(0)


# n개의 주사위를 던졌을 때 경우의 수
n = int(input())
path = [0]*n

def abc(level):
    if level == n:
        for i in range(n):
            print(path[i], end=' ')
        print()
        return

    for i in range(6):
        path[level] = i+1
        abc(level+1)
abc(0)

























