T = int(input())

for tc in range(1, T+1):
    st = input()
    lst = ['(',')','{','}']
    pair = {'}': '{', ')': '(', '{':'}', '(':')'}
    stack = []

    for s in st:
        if s in lst:
            if len(stack)==0 or stack[-1] != pair[s]:
                stack.append(s)
            else: stack.pop()
        else:
            continue

    if len(stack) == 0:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')
