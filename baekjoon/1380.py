tc = 0

while True:
    tc += 1

    num = int(input())
    if num == 0:    # 0 입력 시 반복문 종료
        break

    students = [input() for _ in range(num)]
    bucket = [0]*num    # DAT 이용, 학생들 번호를 인덱스로 수 세기
    for i in range(2*num-1):
        n, a = map(str, input().split())
        bucket[int(n)-1] += 1
    for j in range(num):
        if bucket[j] < 2:   # 한번만 나온 학생 번호 구하기
            name = students[j]

    print(tc, name)
