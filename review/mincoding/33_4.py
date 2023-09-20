n, k = map(int, input().split())
# n 품목 리스트 개수 // k 고기 개수

arr = [0]*(k+1)
edge = []
for _ in range(n):
    a, b = map(str, input().split())
    if a.isdigit() and b.isdigit():
        edge.append((int(a), int(b)))
    elif a.isdigit():
        arr[int(a)] = b
    elif b.isdigit():
        arr[int(b)] = a

f = [0]*(k+1)
def findboss(mem):
    global f
    if f[mem] == 0:
        return mem
    ret = findboss(f[mem])
    return ret

def union(a, b):
    global f
    fa, fb = findboss(a), findboss(b)
    if fa == fb:
        return
    f[fb] = fa
    return f

for i in range(len(edge)):
    union(edge[i][0], edge[i][1])

for i in range(1, k+1):
    if arr[i] == 0:
        x = findboss(i)
        arr[i] = arr[x]
    print(arr[i], end='')