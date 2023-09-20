lst = input()

st = 0
ed = 9
MAX = -1
while st <= ed:
    md = (st+ed)//2
    if lst[md] == '_':
        ed = md-1
    elif lst[md] == '#':
        st = md+1
        MAX = md

print(f'{(MAX+1)*10}%')