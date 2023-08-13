# # 중복순열
#
# card = ['A','B','C','D']
# n = 3
# path = [' '] * n
#
# def abc(level):
#     if level == n:
#         for i in range(n):
#             print(path[i], end='')
#         print()
#         return
#
#     for i in range(4):
#         path[level] = card[i]
#         abc(level+1)
#
# abc(0)



# # 순열 (금, 은, 동)
#
# card = ['A','B','C','D']
# n = 3
# path = [' '] * n
# used = [0]*4
#
# def abc(level):
#     if level == n:
#         for i in range(n):
#             print(path[i], end='')
#         print()
#         return
#
#     for i in range(4):
#         if used[i] != 0: continue
#         path[level] = card[i]
#         used[i] = 1
#         abc(level+1)
#         used[i] = 0
#
# abc(0)



# # 조합 (1)
# n = 3
# path = ['']*n
# card = ['A','B','C','D']
#
# def abc(level):
#     if level == n:
#         for i in range(n):
#             print(path[i],end='')
#         print()
#         return
#
#     for i in range(4):
#         if level>0 and path[level-1] >= card[i]:continue    # 지금 가진 카드보다 더 뒤에 카드들만 탐색할 거야
#         path[level] = card[i]
#         abc(level+1)
#
# abc(0)

# # 조합 (2)
# n = 3
# path = ['']*n
# card = ['A','B','C','D']
#
# def abc(level, start):
#     if level == n:
#         for i in range(n):
#             print(path[i],end='')
#         print()
#         return
#
#     for i in range(start,4):
#         path[level] = card[i]
#         abc(level+1, i+1)   # 탐색하는 리스트 인덱스를 하나씩 뒤로
#
# abc(0, 0)

# # 응용
#
# n = 3
# card = ['A','B','C','D']
# path = ['']*n
#
# def abc(level):
#     # if level == 1 and path[level-1]=='B': return
#       # 진입 후 B로 시작한다면, 리턴해서 뺄 거야
#     if level == n:
#         for i in range(n):
#             print(path[i], end='')
#         print()
#         return
#
#     for i in range(4):
#         if level == 0 and i == 1: continue
#           # B로 시작하는 조합은 뺄 거야
#         path[level] = card[i]
#         abc(level+1)
#
# abc(0)



# # 응용
# n = 3
# card = ['A','B','C','D']
# path = ['']*n
#
# def abc(level):
#     # if level>1 and path[level-1]==path[level-2]: return    # 진입 후 앞뒤 카드가 같다면, 리턴해서 뺄 거야
#     if level == n:
#         for i in range(n):
#             print(path[i],end='')
#         print()
#         return
#
#     for i in range(4):
#         if level != 0 and path[level-1] == card[i]: continue
#         path[level] = card[i]
#         abc(level+1)
#
# abc(0)



# 응용
n = 3
card = ['A','B','C','D']
path = ['']*n

def abc(level):
    # if level>0 and path[level-1]=='C': return     # 진입 후 C 만나면 리턴!
    if level == n:
        for i in range(n):
            print(path[i],end='')
        print()
        return

    for i in range(4):
        if i == 2: continue
        path[level] = card[i]
        abc(level+1)

abc(0)








