a = 13
b = bin(a)  # 2진수
c = oct(a)  # 8진수
d = hex(a)  # 16진수
print(b, c, d)
print(type(b), type(c), type(d))
print(int(b, 2), int(c, 8), int(d, 16))

# 10진수를 n진수로 바꾸기

def trans(mok):
    ans = ''
    while mok >= 1:
        mok, rest = divmod(mok, 2)
        ans += str(rest)
    return ans[::-1]

print(trans(13))

# 비트 연산자
print(13&9)     # 2진수 and
print(13|9)     # 2진수 or
print(13^9)     # 2진수 둘이 다르면 T, 같으면 F

print(10<<2)
print(10>>2)