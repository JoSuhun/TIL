strs=['A', 'E', 'I', 'O', 'U']

while True:
    sentence=input()
    count=0
    if sentence=='#':
        break
    for i in sentence:
        if i.upper() in strs: count+=1
    print(count)