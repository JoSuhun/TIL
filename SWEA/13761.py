T = int(input())

for tc in range(1, T+1):
    st, target = map(str, input().split())

    cnt = len(st)

    for i in range(len(st)-len(target)+1):
        flag = 1
        for j in range(len(target)):
            if st[i+j] != target[j]:
                flag = 0
                break

        if flag == 1:
            cnt = cnt - len(target) +1

    print(f'#{tc} {cnt}')