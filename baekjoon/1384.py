tc = 0
while True:
    tc += 1

    num = int(input())
    if num == 0:
        break
    print(f'Group {tc}')
    arrs = [input().split() for _ in range(num)]
    flag = 0

    for i in range(num):
        for j in range(num):
            if arrs[i][j] == 'N':
                flag += 1
                ni = i-j
                if ni < 0:
                    ni = i + (num-j)
                print(f'{arrs[ni][0]} was nasty about {arrs[i][0]}')

    if flag == 0:
        print('Nobody was nasty')

    print()
