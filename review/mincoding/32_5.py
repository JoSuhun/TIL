n = int(input())
lst = [input() for _ in range(n)]
ans = sorted(lst, key=lambda x: (len(x),x))
for a in ans:
    print(a)