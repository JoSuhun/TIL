# numbers = [6, 10, 2]
numbers = [3, 30, 34, 5, 9]

def solution(numbers):
    answer = ""
    # 문자열에서의 대소비교(sort 정렬 기준)는 문자열 첫 번째 인덱스를 아스키 숫자로 바꿔 비교하고, 같으면 다음 인덱스를 비교하는 형식
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3,reverse=True)

    for num in numbers:
        answer += num

    return str(int(answer))

print(solution(numbers))