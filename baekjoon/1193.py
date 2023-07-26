X = int(input())

total = 0
i = 1

while X > total:    # 2>0   # 2>1
    total += i      # 1     # 3
    i += 1          # 2     # 3

cnt = total - X     # cnt = 1

if i % 2 == 1:
    print(f'{i-1-cnt}/{1+cnt}')
else:
    print(f'{1+cnt}/{i-1-cnt}')



# 아직 이해 못했음
