N = int(input())

num_lst = []
for _ in range(N):
    num_lst.append(int(input()))

num_lst = sorted(num_lst)

for num in num_lst:
    print(num)
