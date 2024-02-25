jobs = [[0, 3], [1, 9], [2, 6]]
import heapq

def solution(jobs):
    answer, ready, now = 0
    start = -1
    heap = []

    while ready < len(jobs):
        for job in jobs:
            if start < now <= ready:
                heapq.heappush([job[1], job[0]])
        if len(heap) > 0:
            cur = heapq.heappop()
            start = now
            now += cur[0]
            answer += (now-cur[1])
            ready += 1
        else:
            now += 1
    return answer


print(solution(jobs))