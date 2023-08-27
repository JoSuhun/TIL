n = int(input())
# n!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수?

def fact(n):
    if n > 1:
        return n * fact(n-1)
    else:
        return 1
ret = fact(n)


now = 1
cnt = 0
while True:
    if ret % now != 0:
        print(cnt-1)
        break
    now *= 10
    cnt += 1