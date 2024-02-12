# 소수찾기
def isPrime(num):
    if num in [2, 3, 5, 7]:
        return True
    if num in [0, 1]:
        return False
    for i in range(2, int(num**0.5)+1):
        if num%i == 0:
            return False
    return True

def solution(numbers):
    answer = []

    def find(length, used, path):
        if length == len(path):
            new = int(path)
            if isPrime(new) & (new not in answer):
                answer.append(new)
            return
        for i in range(len(numbers)):
            if used[i]: continue
            used[i] = 1
            find(length, used, path+numbers[i])
            used[i] = 0

    for i in range(len(numbers)):
        used = [0]*len(numbers)
        find(i+1, used, "")

    return len(answer)