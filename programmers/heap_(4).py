prices = [5, 1, 1, 1, 1]
from collections import deque
def solution(prices):
    answer = []
    for i in range(len(prices)-1):
        cnt = 0
        for j in range(i+1, len(prices)):
            if prices[i] > prices[j]:
                cnt = j-i
                break
            cnt += 1
        answer.append(cnt)
    answer.append(0)
    return answer

print(solution(prices))