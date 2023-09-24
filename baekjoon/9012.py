from collections import deque
T = int(input())

for tc in range(1, T+1):
    st = deque(input())
    lst = deque()
    flag = 1
    while st:
        x = st.popleft()
        if x == '(': lst.append('(')
        else:
            if lst and lst[0] == '(': lst.popleft()
            else:
                lst.append(')')

    if lst: print('NO')
    else: print('YES')