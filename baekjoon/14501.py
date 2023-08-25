n = int(input())
scd = [list(map(int, input().split())) for _ in range(n)]
print(scd)
lst=[]
MAX = -1

def choice(start, SUM):
    global lst, MAX, sum

    for i in range(start, n):
        if start+scd[i][0] <= n-1:
            print(start+scd[i][0],SUM+scd[i][1])
            choice(start+scd[i][0],SUM+scd[i][1])
        else:
            lst.append(SUM)
            return

choice(0,0)
print(lst)