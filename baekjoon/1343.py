board = input()
board_lst = list(board.split('.'))

flag = 0

for i in range(len(board_lst)):
    if len(board_lst[i]) % 4 == 0:
        board_lst[i] = 'AAAA' * (len(board_lst[i])//4)
    elif len(board_lst[i]) % 4 == 2:
        board_lst[i] = 'AAAA' * (len(board_lst[i])//4) + 'BB'
    elif len(board_lst[i]) % 2 == 0:
        board_lst[i] = 'BB' * (len(board_lst[i])//2)
    else:
        flag = 1

if flag == 1:
    print(-1)
else:
    print(*board_lst, sep='.')
