s, p = map(int, input().split())
# 총 문자열 길이 s // 부분 문자열 길이 p
dna_lst = list(input())
checkList = list(map(int, input().split()))

myList = [0]*4      # A C G T
cnt = 0

def add(new):   # 새로운 문자열 들어왔을 때
    global checkList, myList, cnt
    if new == 'A':
        myList[0] += 1
        if myList[0] == checkList[0]:
            cnt += 1
    elif new == 'C':
        myList[1] += 1
        if myList[1] == checkList[1]:
            cnt += 1
    elif new == 'G':
        myList[2] += 1
        if myList[2] == checkList[2]:
            cnt += 1
    elif new == 'T':
        myList[3] += 1
        if myList[3] == checkList[3]:
            cnt += 1

def remove(new):
    global checkList, myList, cnt
    if new == 'A':
        if myList[0] == checkList[0]:
            cnt -= 1
        myList[0] -= 1
    elif new == 'C':
        if myList[1] == checkList[1]:
            cnt -= 1
        myList[1] -= 1
    elif new == 'G':
        if myList[2] == checkList[2]:
            cnt -= 1
        myList[2] -= 1
    elif new == 'T':
        if myList[3] == checkList[3]:
            cnt -= 1
        myList[3] -= 1

for i in range(4):
    if checkList[i] == 0:
        cnt += 1


ret = 0
for i in range(p):
    add(dna_lst[i])
if cnt == 4:
    ret += 1
print(ret)

for i in range(p,s):
    j = i-p
    add(dna_lst[i])
    remove(dna_lst[j])
    print(cnt)
    if cnt == 4:
        ret += 1
print(ret)