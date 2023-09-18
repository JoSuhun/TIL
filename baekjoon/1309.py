n = int(input())

SUM = 0
def make(now, a, b):
    global SUM
    if now == n:
        print(SUM%9901)
        return

    new_a = a+b*2
    new_b = a+b
    SUM = 2*new_a + 3*new_b
    make(now+1, new_a, new_b)

make(1, 0, 1)