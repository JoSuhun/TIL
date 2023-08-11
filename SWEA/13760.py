T = int(input())
for tc in range(1,T+1):
    arr = list(input())

    SUM = 0
    start = 0
    n = 0
    while True:
        for i in range(start,len(arr)):
            if arr[i] == '(' and arr[i+1] == ')':
                SUM += n
                break
            elif arr[i] == '(':
                n += 1
            elif arr[i] == ')':
                SUM += 1
                n -= 1
        start = i + 2
        if start == len(arr)-1:
            break

    print(f'#{tc} {SUM+1}')