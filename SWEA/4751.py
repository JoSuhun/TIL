T = int(input())
for tc in range(T):
    st=input()
    n = len(st)


    arrs = [[' '] for _ in range(5)]

    lst = ['.','.','#','.','.']
    for i in range(5):
        arrs[i][0] = lst[i]

    for i in range(n):

        arr1 = ['.','#','.','.']
        arrs[0].extend(arr1)
        arrs[4].extend(arr1)

        arr2 = ['#','.']*2
        arrs[1].extend(arr2)
        arrs[3].extend(arr2)

        arr3 = ['.',st[i],'.','#']
        arrs[2].extend(arr3)


    for i in arrs:
        print(''.join(i))