bridge_length = 100
weight = 100
truck_weights = [10,10,10,10,10,10,10,10,10,10]

from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 1
    onbridge = deque()
    ready = deque(truck_weights)
    new = ready.popleft()
    onbridge.append([new, answer])
    temp = new
    done = 0
    while onbridge:
        answer += 1
        if answer == bridge_length + onbridge[0][1]:
            temp -= onbridge[0][0]
            onbridge.popleft()
            done += 1
        if ready:
            if (temp + ready[0] <= weight) and (len(onbridge) < bridge_length):
                new = ready.popleft()
                onbridge.append([new, answer])
                temp += new

    return answer

print(solution(bridge_length, weight, truck_weights))