st = list(input())
n = len(st)
ans = ['']*n
print(*st, sep='')
while True:
    if st == list('_'*n):
        break
    for i in range(n):
        if st[i] == '_':continue
        if ord(st[i])-1<65:
            st[i] = '_'
        else:
            st[i]= chr(ord(st[i])-1)
    print(*st, sep='')

