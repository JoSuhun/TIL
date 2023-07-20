T = int(input())

for tc in range(T):
    N, M = map(int, input().split())

    def fact(M):
        if M == 0:
            return 1
        return M * fact(M-1)
    print(fact(M))