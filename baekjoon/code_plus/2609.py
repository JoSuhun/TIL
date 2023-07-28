# import math

# a, b = map(int, input().split())

# print(math.gcd(a,b))
# print(math.lcm(a,b))


# 유클리드 호제법?
# 최대공약수란, 숫자 a,b가 주어졌을 때, 공통되는 약수 중에서 최대 값을 의미한다.
# 2개의 자연수

a, b = map(int, input().split())

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

print(gcd(a,b))
print(lcm(a,b))