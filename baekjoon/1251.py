st = input()
<<<<<<< HEAD

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
=======
st_lst = list(st)
sorted_lst = sorted(st_lst)
st1 = st_lst[:st_lst.index(sorted_lst[0])+1]
st2 = st_lst[st_lst.index(sorted_lst[0])+1:st_lst.index(sorted_lst[1])+1]
st3 = st_lst[st_lst.index(sorted_lst[1])+1:]

st1_re = st1[::-1]
st2_re = st2[::-1]
st3_re = st3[::-1]

result = [*st1_re, *st2_re, *st3_re]
for re in result:
    print(re,end='')
>>>>>>> 1607b1ea23e6f94a15ec3a82f387d51ad4d10667
