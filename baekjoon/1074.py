n, r, c = map(int, input().split())

def make(n, r, c):
    if n == 0:
        return 0
    return r%2*2 + c%2 + 4 * make(n-1, r//2, c//2)
print(make(n, r, c))
