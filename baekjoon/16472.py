n = int(input())    # 문자열 종류 개수
strs = list(input())

st = 0
MAX = -1
while True:
    total = 0
    lst = []
    for i in range(st, len(strs)):
        if strs[i] in lst:
            total +=1
        if strs[i] not in lst:
            lst.append(strs[i])
            if len(lst)>n: break
            total+=1

    st +=1
    if st>len(strs)-1:
        break
    MAX = max(total, MAX)

print(MAX)

# 시간초과
