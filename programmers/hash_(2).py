# 전화번호 목록
phone_book = ["123","456","789"]

def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        num = phone_book[i]
        next = phone_book[i+1]
        if num == next[:len(num)]:
            answer = False
            return answer
    return answer
print(solution(phone_book))