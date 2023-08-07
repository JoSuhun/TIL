T = int(input())
for tc in range(1, T+1):
    str1 = list(input())
    str2 = list(input())

    dic = {}

    for st in str2:
        dic[st] = dic.get(st, 0)+1

    MAX = -21e8
    for st in str1:
        if dic[st] > MAX:
            MAX = dic[st]
    print(f'#{tc} {MAX}')
