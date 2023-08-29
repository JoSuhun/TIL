n = int(input())
ids = [input() for _ in range(n)]

ans = []
for id in ids:
    if id[0].isupper() and id[1:].islower():
        ans.append(id)
    elif id.islower():
        ans.append(id[0].upper() + id[1:])
    else:
        ans.append(id.upper())
ans.sort()
for a in ans:
    print(a)