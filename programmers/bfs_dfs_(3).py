# 타겟 넘버

def solution(numbers, target):
    answer = 0

    def make(idx, total):
        nonlocal answer
        if idx == len(numbers):
            if total == target: answer += 1
            return
        make(idx+1, total+numbers[idx])
        make(idx+1, total-numbers[idx])

    make(0, 0)
    return answer
