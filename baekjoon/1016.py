MIN, MAX = map(int, input().split())

numlst = [0]*(MAX+1)
for i in range(MIN, MAX+1):
    numlst[i] = 1
for i in range(2, int(MAX**0.5)+1):
    print(i)
    if numlst[i] == 1:
        for j in range(i*i, MAX+1, i*i):
            numlst[j] = 0

print(numlst.count(1))