def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

T = int(input())
for tc in range(1, T+1):
    a, b = map(int, input().split())
    print(int(a*b/gcd(a,b)))
