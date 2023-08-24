n = int(input())    # n 시험장 개수
a_lst = list(map(int, input().split()))    # n개의 시험장의 각 응시자 수
b, c = map(int, input().split())    # b 총감 응시자 수 // c 부감 응시자 수

for i in range(n):
    a_lst[i] -=b

SUM = n
for i in range(n):
    if a_lst[i] <= 0: continue
    elif a_lst[i] <= c: SUM += 1
    else:
        SUM += (a_lst[i] // c)
        if a_lst[i] % c:
            SUM += 1

print(SUM)