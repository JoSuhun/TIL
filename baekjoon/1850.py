def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

a, b = map(int, input().split())
ret = gcd(a, b)
print('1'*ret)