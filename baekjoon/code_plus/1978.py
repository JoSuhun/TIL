def prime_list(n):
    arr = [True]*n

    m = int(n**2)

    for i in range(2, m+1):
        if arr[i] == True:
            for j in range(i+i, n, i):
                arr[j] = False
                