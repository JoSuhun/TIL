idx, age = map(int, input().split())

def move(age, now):
    arr = ['_','_','_','_','_']
    if age == 0 or now>4:
        print('_____')
        return

    arr[now] = age
    print(*arr, sep='')
    move(age-1, now+1)

move(age, idx)