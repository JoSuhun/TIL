st = input()
<<<<<<< HEAD
st_lst = list(st)
sorted_lst = sorted(st_lst)
sorted_lst[0]
=======
>>>>>>> 4af8427d0ee573b183c71e0f6350cac8c1823cfb

lst = []

for i in range(1, len(st)-2):   # 한 번 자르기
    for j in range(i+1, len(st)):   # 두 번 자르기
        st1 = st[:i]
        st2 = st[i:j]
        st3 = st[j:]
        re_st1 = st1[::-1]
        re_st2 = st2[::-1]
        re_st3 = st3[::-1]
        lst.append(re_st1+re_st2+re_st3)

print(sorted(lst)[0])
