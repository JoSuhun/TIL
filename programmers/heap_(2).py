jobs = [[0, 3], [1, 9], [2, 6]]
import heapq, math

def solution(jobs):

    answer = 0
    total, ready, start = 0, 0, -1 # total 종료 시간, ready 요청 들어온 시간
    level = len(jobs)
    heap = []
    
    while ready < level:
        for job in jobs:
            heapq.heappush(heap, [job[1],job[0]]) # 소요시간이 짧은 순서대로 heap 정렬
        while heap:
            if start <= ready <= total:
                disk = heapq.heappop() # [소요시간, 요청 들어온 시간]
                total += disk[0]
                

    

    return answer

print(solution(jobs))