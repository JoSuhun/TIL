import heapq
from collections import deque
def solution(priorities, location):
    answer = 1
    q = deque()
    for i in range(len(priorities)):
        q.append((priorities[i], i))
    while q:
        listq = list(q)
        listq.sort(key=lambda x: x[0])
        MAX = listq[-1][0]
        now, idx = q.popleft()
        if now >= MAX:
            if idx == location:
                break
            else:
                answer += 1
        else:
            q.append((now, idx))
    return answer

print(solution(priorities, location))