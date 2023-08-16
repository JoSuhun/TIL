T = int(input())
for tc in range(1, T+1):
    arr = list(map(str, input().split()))

    def make(x, y, msg):
        if msg == '+':
            return x+y
        elif msg == '*':
            return x*y
        elif msg == '-':
            return x-y
        elif msg == '/':
            return x//y

    cal = ['+', '*', '-', '/']
    stack = []

    while True:
        try:
            if arr[0] not in cal and arr[0] != '.':
                stack.append(int(arr[0]))
                arr.pop(0)

            elif arr[0] in cal:
                i = stack.pop(-1)
                j = stack.pop(-1)
                msg = arr[0]
                ret = make(j, i, msg)
                stack.append(ret)
                arr.pop(0)

            elif arr[0] == '.': break

        except: break

    if len(stack) != 1:
        print(f'#{tc} error')
    else:
        print(f'#{tc} {stack[0]}')
