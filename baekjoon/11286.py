# from collections import deque
#
# q = deque()
#
# n = int(input())
# for i in range(n):
#     x = int(input())
#     if x != 0:
#         q.append(x)
#         q = sorted(q, key=lambda x: (abs(x), x))
#         q = deque(q)
#     if x == 0:
#         if q:
#             ret = q.popleft()
#             print(ret)
#         else:
#             print(0)


# 우선순위 큐
from queue import PriorityQueue
import sys
print = sys.stdout.write
input = sys.stdin.readline

q = PriorityQueue()

n = int(input())
for i in range(n):
    x = int(input())
    if x != 0:
        q.put((abs(x), x))
    else:
        if q.empty():
            print('0\n')
        else:
            ret = q.get()
            print(str(ret[1])+'\n')