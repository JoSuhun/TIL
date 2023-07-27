st = input()
st_lst = list(st)
sorted_lst = sorted(st_lst)
sorted_lst[0]

st1_re = st1[::-1]
st2_re = st2[::-1]
st3_re = st3[::-1]

result = [*st1_re, *st2_re, *st3_re]
for re in result:
    print(re,end='')
