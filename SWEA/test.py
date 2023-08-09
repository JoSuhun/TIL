arr = [1,2,3,4]
n = int(input())
path = [' '] * n

def abc(level):
    if level == n:
        for i in range(n):
            print(path[i], end='')
        print()
        return

    for i in range(4):
        path[level] = i+1
        abc(level+1)

abc(0)