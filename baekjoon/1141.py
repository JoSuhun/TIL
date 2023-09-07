n = int(input())
lst = [input() for _ in range(n)]
lst = sorted(lst, key=lambda x: len(x))

total = 0
now = 0
while lst:
    a = lst.pop(0)
    end = len(a)
    for i in range(len(lst)):
        if a == lst[i][:end]:
            n-=1
            break
print(n)