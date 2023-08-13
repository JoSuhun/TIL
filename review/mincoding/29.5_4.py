a = list(map(int, input().split()))
b = list(map(int, input().split()))

result = []

def make(a, b):
    global result

    if len(a) == 0 or len(b) == 0: return
    if a[0] > b[0]:
        result.append(b[0])
        b.pop(0)
    else:
        result.append(a[0])
        a.pop(0)
    make(a,b)

make(a,b)

if len(a) != 0:
    result.extend(a)
elif len(b) != 0:
    result.extend(b)

print(*result)