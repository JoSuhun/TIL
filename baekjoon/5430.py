from collections import deque
T = int(input())

for tc in range(T):
    msg = input()
    n = int(input())
    st = deque(input()[1:-1].split(','))
    if n == 0:
        st = deque()


    rev = 0
    for m in msg:
        if m == 'R':
            rev += 1
        elif m == 'D':
            if len(st) > 0:
                if rev%2==1:
                    st.pop()
                else: st.popleft()
            else:
                print('error')
                break
    else:
        if rev%2 == 0:
            print('[' + ','.join(st) + ']')
        else:
            st.reverse()
            print('[' + ','.join(st) + ']')