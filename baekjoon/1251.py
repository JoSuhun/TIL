st = input()

lst = []
for i in range(1, len(st)-2):
    for j in range(i+1, len(st)):
        st1 = st[:i]
        st2 = st[i:j]
        st3 = st[j:]
        re_st1 = st1[::-1]
        re_st2 = st2[::-1]
        re_st3 = st3[::-1]
        lst.append(re_st1+re_st2+re_st3)

print(sorted(lst)[0])
