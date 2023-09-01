T = int(input())


for tc in range(1, T+1):
    num1 = list(input())
    num2 = list(input())

    lst1 = [0] * len(num1)
    backup1 = num1[:]
    for i in range(len(num1)):
        if num1[i] == '1':
            num1[i] = '0'
        elif num1[i] == '0':
            num1[i] = '1'
        new = ''.join(num1)
        lst1[i] = int(new,2)
        num1 = backup1[:]

    lst2 = []
    backup2 = num2[:]
    nums = ['0', '1', '2']
    def make(now):
        for i in range(3):
            if num2[now] == nums[i]: continue
            num2[now] = nums[i]
            new = ''.join(num2)
            lst2.append(int(new, 3))

    for i in range(len(num2)):
        make(i)
        num2 = backup2[:]
    make(0)

    flag = 0
    for i in range(len(lst1)):
        for j in range(len(lst2)):
            if lst1[i] == lst2[j]:
                flag = 1
                print(f'#{tc} {lst1[i]}')
                break
        if flag: break