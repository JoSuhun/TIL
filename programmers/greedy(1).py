# 체육복
n = 5
lost = [3, 5]
reserve = [2, 4]

def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    answer = n - len(lost)

    for i in len(reserve):
        for j in len(lost):
            if reserve[i]==lost[j]:
                answer += 1
                reserve[i] = -1
                lost[j] = -1

    for i in reserve:
        if i-1 in lost:
            answer += 1
            lost.remove(i-1)
        elif i+1 in lost:
            answer += 1
            lost.remove(i+1)

    return answer

print(solution(n, lost, reserve))