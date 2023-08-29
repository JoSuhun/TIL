arrs = ['ABCD','ABCE','AGEH','EIEI','FEQE','ABAD']

key = input()
idx = [0]*4
for i in range(4):
    if key[i] != '?':
        idx[i] = key[i]

cnt = 0
for arr in arrs:
    flag = 0
    for i in range(4):
        if idx[i] != 0:
            if idx[i] == arr[i]:
                flag = 1
            else: flag = 0
    cnt += flag
print(cnt)