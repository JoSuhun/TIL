first = [1, 2, 3, 4, 5]*2000
second = [2, 1, 2, 3, 2, 4, 2, 5] *1250
third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] *1000

def solution(answers):
    people = [0]*3
    MAX = -1
    answer = []
    for i in range(len(answers)):
        if first[i] == answers[i]: people[0]+=1
        if second[i] == answers[i]: people[1]+=1
        if third[i] == answers[i]: people[2]+=1
    for i in range(3):
        if people[i] >= MAX:
            MAX = people[i]
    for i in range(3):
        if people[i] == MAX:
            answer.append(i+1)
    return answer
