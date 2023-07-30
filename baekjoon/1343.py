# 폴리오미노, AAAA, BB

board = input()
board_lst = list(board.split('.'))

result = []

for x in board_lst:

    if x == '':
        pass
    elif len(x) % 4 == 0:
        x = 'AAAA' * (len(x)//4)
    elif len(x) % 6 == 0 or len(x) % 10 == 0:
        x = ('AAAA' * (len(x)//4)) + 'BB'
    elif len(x) % 2 == 0:
        x = 'BB'
    else:
        x = 'NO'

    result.append(x)

result = '.'.join(result)


cnt = 0
for _ in result:
    if _ == '.':
        cnt += 1


if cnt == len(result):
    print('.'*len(result))
elif 'NO' in result:
    print('-1')
else:
    print(result)


# 반례 못찾겠음 흑흑
