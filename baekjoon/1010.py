T = int(input())


def fact(i):
    if i == 0:
        return 1
    return i * fact(i-1)


for tc in range(T):
    N, M = map(int, input().split())

    fact_N = fact(N)
    fact_M = fact(M)
    fact_MN = fact(M-N)

    print(int(fact_M / (fact_N * fact_MN)))

    # M!
    # N!
    # (M-N)!
    # def factorial(n):
    # if n == 0:          # 무한 호출을 조심해!
    # 	return 1
    # return n * factorial(n-1)
