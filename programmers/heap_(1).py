# 더 맵게

scoville = [1, 2, 3, 9, 10, 12]
K = 7
import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0

    while True:
        x = heapq.heappop(scoville)
        if x >= K: break
        if len(scoville)==0:
            answer = -1
            break
        y = heapq.heappop(scoville)
        heapq.heappush(scoville, x+(2*y))
        answer += 1
    return answer

print(solution(scoville, K))