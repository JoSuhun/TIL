# [swap]
a, b = 3, 5    # 할당할 거야

temp = a    # temp는 빈 컵
a = b
b = temp
# a, b = b, a 를 해도 같은 값 나온다!

print(a, b)    # 5 3



# [boolean]
a, b = 0, -1
a = bool(a)
b = bool(b)
print(a, b)    # False True    # 0이외의 정수값은 True

x=''
y='asdf'
print(bool(x), bool(y))    # False True    # 빈 문자열은 False



# [파이썬의 부동소수점 고정소수점]
a = 3.14
print(type(a))

print(round(a, 1))    # 소수점  첫번째 자리까지 출력    # round는 반올림
                                                      # math.floor 내림
                                                      # math.ceil 올림
print(f'{a:.1f}')    # 소수점 몇번째 자리까지 실수로 출력할 것인고

print(round(0.5))    # 0
print(round(1.5))    # 2
print(round(2.5))    # 2
print(round(3.5))    # 4
print(round(4.5))    # 4
print(round(5.5))    # 6
# 소수점 첫째 자리가 5일 때, 정수값이 홀수일 때만 해줌 ;;
# 소수점 첫째 자리가 4이하일 때, 내림
# 소수점 첫째 자리가 6이상일 때, 반올림

print(round(0.05, 1))    # 0.1
print(round(0.15, 1))    # 0.1
print(round(0.25, 1))    # 0.2
print(round(0.35, 1))    # 0.3
print(round(0.45, 1))    # 0.5
print(round(0.55, 1))    # 0.6
# 소수점 둘째 자리에서 반올림할 경우, 오사오입 통하지 않음
# 파이썬이 부동소수점을 이용해서 실수를 표현하므로, 정확한 값이 아닌 근사값으로 계산을 함
# 정확한 계산 못함 ㅇㅁㅇ

print(round(0.50000,1))    # 0.5
print(round(1.50000,1))    # 1.5
print(round(2.50000,1))    # 2.5
print(round(3.50000,1))    # 3.5
print(round(4.50000,1))    # 4.5
print(round(5.50000,1))    # 5.5


# 그래서 ........ 반올림 하라고 했을 때 어떻게 처리하는지?
# 1. 값에 +0.5를 하고 내림처리 하기.. 오
import math
print(math.floor(0.5+0.5))    # 1
print(math.floor(1.5+0.5))    # 2
print(math.floor(2.5+0.5))    # 3
print(math.floor(3.5+0.5))    # 4
print(math.floor(4.5+0.5))    # 5
print(math.floor(5.5+0.5))    # 6

# 2. 꼼수같은 방법! 임의의 작은 수를 더해버리자 (보너스# 지수 표기법)
print(round(0.05 + 1e-10, 1))    # 0.1
print(round(0.15 + 1e-10, 1))    # 0.2
print(round(0.25 + 1e-10, 1))    # 0.3
print(round(0.35 + 1e-10, 1))    # 0.4
print(round(0.45 + 1e-10, 1))    # 0.5
print(round(0.55 + 1e-10, 1))    # 0.6



# [문자열]

# [순서 있음] -> list, tuple, range
# (string)
s = "abcdefg"
print(s[:3])    # abc
print(s[3:])    # defg
print(s[2:5])    # cde
print(s[5:2:-1])    # fed
print(s[2:5:2])    # ce
print(s[::-1])    # gfedcba
print(s[-2])    # f

st='asdfgh'
    # st[2] = 'dddddd'
    # print(st)    # 안되지롱

# (list)
lst=[1, 2, 3, 4, [5, 6, 7], 8]
print(lst[4][0])    # 5
print(lst[-2][-3])    # 5

print(list(range(3)))
print(list(range(3, 6)))
print(list(range(3, 8, 2)))    # 3부터 8까지 2씩 증가

# (tuple)
tp = (1, 2, 3, 4, 5)
print(tp)
print(len(tp))
print(tp[1])
print(tp[-1])


# [순서 없음] -> set, dictionary
# (dictionary)
di={1:3, 2:{4:5}, '학':6, '교':[7,8,9]}
print(di[1])
print(di[2][4])
print(di['학'])
di[2] = 5   # value 바꾸기
print(di)
di[111]=di.pop(1)   # key 바꾸기    # {2: 5, '학': 6, '교': [7, 8, 9], 111: 3}
print(di)

# (set) - 순서 없음. 중복을 제거할 때 유용한 자료형 ('ㅅ')
s={1,2,3,4,5,6}
print(s)
print(type(s))

lst=[1,1,2,3,4,5,1,2,6,3,4,4,6,7,2]
lst=list(set(lst))  # 리스트를 set처리 해줄 수 있다!!
print(lst)

s1={1, 2, 3}
s2={3, 4, 5}
print(s1|s2)    # 합집합
print(s1-s2)    # 차집합
print(s1&s2)  # 교집합



# 논리연산
a = True
b = False
c = True
d = False
print(a and b)  # False
print(a and c)
print(a or b)

x1 = bool(0)     # False
print(a)
x2 = bool('0')   # True
print(b)

print('a' and 'b')      # 둘 다 참이야? 맨 마지막으로 들어간 'b' 뱉어내!
print('' and 'b')       # 앞에 공백인 ''이 False야 뱉어낼 거 없음.
print(0 and 1)

vowels = 'aeiou'

print(('a' and 'b') in vowels)      # False
print(('b' and 'a') in vowels)      # True


# [연산자 우선순위]
what = -3 ** 2
print(what)

# [객체 비교하는 is]
a = 2
b = 2.0
if a == b:
    print('정답')
else:
    print('오답')   # 값 비교

a = 2
b = 2.0
if a is b:
    print('정답')
else:
    print('오답')   # 객체 비교 !!!!!!!!!!!!!!!