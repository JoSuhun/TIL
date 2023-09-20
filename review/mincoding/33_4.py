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

