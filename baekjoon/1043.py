def findboss(mem):
    global arr
    if arr[mem] == mem:
        return mem
    ret = findboss(arr[mem])
    arr[mem] = ret
    return ret

def union(a, b):
    global arr
    fa, fb = findboss(a), findboss(b)
    if fa == fb:
        return
    arr[fb] = fa

n, m = map(int, input().split())
# n 사람 수 // m 파티 수
true = list(map(int, input().split()))
trueN = true.pop(0)
check = [0]*(n+1)
for i in range(trueN):
    check[true[i]] = 1

arr = [i for i in range(n+1)]
partyList = [[] for _ in range(m)]
for i in range(m):
    party = list(map(int, input().split()))
    partyN = party.pop(0)
    partyList[i] = party

    if partyN >1:
        for i in range(partyN-1):
            a = party[i]
            b = party[i+1]
            union(a, b)

cnt = m
for i in range(trueN):
    true[i] = findboss(true[i])

for p in partyList:
    for i in p:
        if findboss(i) in true:
            cnt -= 1
            break
print(cnt)
