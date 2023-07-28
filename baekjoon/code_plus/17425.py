import sys

T = int(sys.stdin.readline())

for tc in range(T):

    N = int(sys.stdin.readline())
    total = 0

    for i in range(1, N+1):
        total += (N//i) * i

    print(total)