n = int(input())    # 문자열 종류 개수
strs = list(input())

st = 0
ed = 1
cnt = 1
MAX = -1
used = [0]*200
while st<=ed:
    used[ord(strs[st])] = 1
    if ed == len(strs)-1:
        if used[ord(strs[ed])] == 1 or cnt+1<=n:
            MAX = max(MAX, ed-st+1)
        elif used[ord(strs[ed])] == 0 and cnt+1>n:
            MAX = max(MAX, ed-st)
        break

    if strs[st] == strs[ed]:
        ed += 1
    elif strs[st] != strs[ed]:
        if used[ord(strs[ed])] == 1:
            ed += 1
        else:
            cnt += 1
            if cnt <= n:
                used[ord(strs[ed])] = 1
                ed += 1
            else:
                MAX = max(MAX, ed-st)
                st +=1
                ed = st
                used = [0]*200
                cnt = 1

print(MAX)