n, msg = map(int,input().split())
msg = list(str(msg))
flag = 1

def password(word):
    global flag

    if flag == 0: return

    for i in range(n-1):
        if word[i] == word[i+1]:
            word.pop(i)
            word.pop(i+1)
            flag = 1
            break
        else: flag = 0
    password(word)


print(msg)