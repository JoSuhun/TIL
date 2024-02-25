bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]

def solution(bridge_length, weight, truck_weights):
    answer = 0
    onbridge = []
    temp = 0

    onbridge.append(truck_weights[0])
    truck_weights.pop(0)

    while onbridge:
        if onbridge[0] >= weight:
            temp += 1
        if temp == bridge_length:
            answer += temp
            temp = 0
        

    return answer