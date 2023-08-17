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






# # 입력받은 좌표에 꽃이 언제 필까?

yy, xx = map(int, input().split())

arrs = [[0]*4 for _ in range(4)]

arrs[2][1] = 1      # 2, 1에 꽃이 피어있어 하루에 인접한 + 방향으로 꽃이 핌

q = deque()
q.append((2, 1, 1))

directy = [0, 0, 1, -1]
directx = [1, -1, 0, 0]
ans = 0

while q:
    y, x, level = q.popleft()

    if y == yy and x == xx:
        ans = level

    for i in range(4):
        dy = y + directy[i]
        dx = x + directx[i]
        if dy<0 or dx<0 or dy>3 or dx>3: continue
        if arrs[dy][dx] != 0: continue
        arrs[dy][dx] = arrs[y][x] +1
        q.append((dy, dx, level+1))

        # if dy == yy and dx == xx:
        #     ans = level+1

print(ans)
for arr in arrs:
    print(*arr)







