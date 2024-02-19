k = 80
dungeons = [[80,20],[50,40],[30,10]]
from collections import deque

def solution(k, dungeons):
    answer = -1
    visit = []
    q = deque()
    q.append((k, visit))

    while q:
        left, visit = q.popleft()
        for i in range(len(dungeons)):
            if left < dungeons[i][0]:
                answer = max(answer, len(visit))
                continue
            if i in visit: continue
            q.append((left-dungeons[i][1], visit+[i]))

    return answer

print(solution(k, dungeons))