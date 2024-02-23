# 구조

people = [20, 20, 30, 90]
limit = 100

def solution(people, limit):
    answer = 0

    people.sort()
    start = 0
    end = len(people)-1

    # 투포인터
    while start<=end:
        now = people[start]
        next = people[end]
        if now + next <= limit:
            answer += 1
            start += 1
            end -=1
        else:
            answer += 1
            end -=1
    
    return answer

print(solution(people, limit))