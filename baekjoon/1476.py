e, s, m = map(int, input().split())

e0 = 0
s0 = 0
m0 = 0
y = 0

while True:
    e0 += 1
    s0 += 1
    m0 += 1
    y += 1
    if e0>15: e0 = 1
    if s0>28: s0 = 1
    if m0>19: m0 = 1

    if e0 == e and s0 == s and m0 == m: break
print(y)
