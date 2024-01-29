# 같은 숫자는 싫어!
from collections import deque

def solution(arr):
    q = deque(arr)
    answer = []
    visited = [0]*10
    while q:
        num = q.popleft()
        if visited[num]: continue
        else:
            visited= [0]*10
            visited[num] = 1
            answer.append(num)
    return answer