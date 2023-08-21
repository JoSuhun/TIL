n, m = map(int, input().split())     # n * m
cnt = int(input())  # 잘라야하는 점선 개수
v = [0]
h = [0]
for i in range(cnt):
    w, num = map(int, input().split())  # 가로 0, 세로 1 // 점선 번호
    if w == 0:
        v.append(num)
    else:
        h.append(num)
v.append(m)
h.append(n)
v.sort()
h.sort()

def size(sty, edy, stx, edx):
    size = (edy-sty) * (edx-stx)
    return size


MAX = -1
for i in range(len(v)-1):
    for j in range(len(h)-1):
        ret = size(v[i], v[i+1], h[j], h[j+1])
        if ret > MAX:
            MAX = ret
print(MAX)