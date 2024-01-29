# 기능개발

progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]
def solution(progresses, speeds):
    answer = []
    temp = 0
    cnt = 0
    while progresses:
        if (progresses[0] + temp * speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
        else:
            if cnt >= 1:
                answer.append(cnt)
                cnt = 0
            else:
                temp += 1
    answer.append(cnt)
    return answer

print(solution(progresses, speeds))