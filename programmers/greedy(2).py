# 큰수 만들기
number = "1231234"
k = 3

def solution(number, k):
    answer = []
    for num in number:
        while k > 0 and answer and answer[-1] < num:
            answer.pop()
            k -= 1
        answer.append(num)

    answer = ''.join(answer[:len(number)-k])
    return answer

print(solution(number, k))