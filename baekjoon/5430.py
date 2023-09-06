T = int(input())

def rev(lst):
    new = [0]*n
    now = 0
    while now<n:
        new[now] = lst[n-1-now]
        now += 1
    return new

def delete(lst):
    lst.pop(0)
    return lst


for tc in range(1, T+1):
    msg = input()
    n = int(input())
    if n == 0:
        print('error')
    else:
        st = input()
        st = st[1:-1]
        q = list(map(int, st.split(',')))
        try:
            for m in msg:
                if m == 'R':
                    q = rev(q)
                elif m == 'D':
                    q = delete(q)
            print('[',end='')
            print(*q, sep=',',end='')
            print(']')
        except:
            print('error')
