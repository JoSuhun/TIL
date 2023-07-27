while True:
    
    try:
        n = int(input())

        i = 1

        while True:
            num = int('1'*i)
            if num % n ==0:
                print(len(str(num)))
                break
            i += 1

    except:
        break