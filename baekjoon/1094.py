n = int(input())
n_bin_st = str(bin(n))
count = 0

for i in n_bin_st:
    if i == '1':
        count += 1

print(count)
