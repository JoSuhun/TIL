L = int(input())    # 롤 케이크 길이
N = int(input())    # 방청객 수

pToK = [list(map(int, input().split())) for _ in range(N)]
expect = []
result = [0]*N

rollCake = [0]*L
for i in range(N):
    st = pToK[i][0]
    ed = pToK[i][1]
    for k in range(st-1, ed):
        if rollCake[k] != 0: continue
        rollCake[k] = i+1

    expect.append(ed-st+1)

for l in rollCake:
    if l == 0: continue
    result[l-1] += 1

def choice(arr):
    for i in range(N):
        if arr[i] >= max(arr):
            print(i+1)
            break

choice(expect)
choice(result)