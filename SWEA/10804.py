T = int(input())

for tc in range(1, T+1):

    st = list(input())

    n_st = ['']*len(st)
    for i in range(len(st)):
        if st[i] == 'q':
            n_st[len(st)-1-i] = 'p'
        elif st[i] == 'p':
            n_st[len(st)-1-i] = 'q'
        elif st[i] == 'b':
            n_st[len(st)-1-i] = 'd'
        elif st[i] == 'd':
            n_st[len(st)-1-i] = 'b'

    print(f"#{tc} {''.join(n_st)}")
