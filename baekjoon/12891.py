s, p = map(int, input().split())
# 총 문자열 길이 s // 부분 문자열 길이 p
dna_lst = list(input())
checkList = list(map(int, input().split()))

mylst = [0]*4
cnt = 0

def add(new):   # 새로운 문자열 추가
    global checkList, mylst, cnt
    if new == 'A':
        mylst[0] += 1
        if mylst[0] == checkList[0]:
            cnt += 1

    elif new == 'C':
        mylst[1] += 1
        if mylst[1] == checkList[1]:
            cnt += 1

    elif new == 'G':
        mylst[2] += 1
        if mylst[2] == checkList[2]:
            cnt += 1

    elif new == 'T':
        mylst[3] += 1
        if mylst[3] == checkList[3]:
            cnt += 1


def remove(new):   # 문자열 제거
    global checkList, mylst, cnt
    if new == 'A':
        if mylst[0] == checkList[0]:
            cnt -= 1
        mylst[0] -= 1

    elif new == 'C':
        if mylst[1] == checkList[1]:
            cnt -= 1
        mylst[1] -= 1

    elif new == 'G':
        if mylst[2] == checkList[2]:
            cnt -= 1
        mylst[2] -= 1

    elif new == 'T':
        if mylst[3] == checkList[3]:
            cnt -= 1
        mylst[3] -= 1

for i in checkList:
    if i == 0:
        cnt += 1

for i in range(p):
    add(dna_lst[i])

result = 0
if cnt == 4:
    result += 1

for i in range(p,s):
    j = i-p
    add(dna_lst[i])
    remove(dna_lst[j])
    if cnt == 4:
        result += 1
print(result)