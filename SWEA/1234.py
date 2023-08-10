def delete(lst):
    end = len(lst)-1
    while end>0:
        for i in range(end):
            if lst[i] == lst[i+1]:
                lst.pop(i)
                lst.pop(i)
                break
        end-=2
    return lst

for tc in range(1,11):
    n, arr = map(str, input().split())
    arr = list(arr)
    ret = delete(arr)
    print(f"#{tc} {''.join(ret)}")