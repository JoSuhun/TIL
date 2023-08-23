T = int(input())
for tc in range(1, T+1):
    students = list(map(int, input().split()))

    tc_num = students.pop(0)

    result = []
    first = students.pop(0)
    result.append(first)

    cnt = 0
    while students:
        flag = 1
        target = students.pop(0)
        for who in result:
            if who > target:
                result.insert(result.index(who), target)
                flag = 0
                cnt += len(result[result.index(who):])
                break
            else: flag = 1
        if flag == 1:
            result.append(target)
    print(f'{tc} {cnt}')
