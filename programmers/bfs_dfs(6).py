# 단어 변환
begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log"]

from collections import deque
def solution(begin, target, words):
    answer = 21e8
    q = deque()
    q.append((begin, 0))
    visit = [0]*len(words)
    while q:
        word, cnt = q.popleft()
        if word == target:
            answer = min(answer, cnt)
        if cnt > answer: continue
        for i in range(len(words)):
            if visit[i] == 1: continue
            equal = 0
            for j in range(len(word)):
                if word[j] == words[i][j]:
                    equal += 1
            if equal == len(word)-1:
                visit[i] = 1
                q.append((words[i], cnt+1))
    if answer == 21e8: return 0
    else: return answer

print(solution(begin, target, words))