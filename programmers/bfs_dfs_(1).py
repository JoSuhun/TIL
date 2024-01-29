# 여행경로
from collections import deque
def solution(tickets):
    answer = []
    tickets.sort(key=lambda x:(x[0], x[1]))
    q = deque([(['ICN'], tickets)])
    while q:
        now, left = q.popleft()

        if len(left) == 0:
            answer = now
            break

        idx = -1
        for i in range(len(left)):
            if left[i][0] == now[-1]:
                idx = i
                break

        if idx == -1: continue
        while idx < len(left) and left[idx][0] == now[-1]:
            q.append((now+[left[idx][1]], left[:idx]+left[idx+1:]))
            idx += 1
    return answer
