# 완주하지 못한 선수
import heapq
def solution(participant, completion):
    answer = ''
    heapq.heapify(participant)
    heapq.heapify(completion)
    while completion:
        a = heapq.heappop(participant)
        b = heapq.heappop(completion)
        if a != b:
            answer = b
            return answer
    answer = participant[0]
    return answer