# [함수]
def abc():  # 함수를 정의
    print('jojojojojosuhun')

for i in range(5):
    abc()   # 함수를 호출

# 두 수의 합을 출력하는 함수
def getSum(a, b):
    return a + b, a * b

ret = getSum(3, 5)
print(ret)  # (8, 15) 튜플로 반환된다 ㅇㅁㅇ, python에서만 가능하다.


def getSum(a, b):
    return 

ret2 = getSum(2, 4)
print(ret2)     # None이 출력된다. 아무 값도 없이 return하면, 걍 함수 꺼지는 거임.

# default parameter
def getSum(a, b, c=20):     # default parameter은 일반 매개변수보다 맨 뒤에
    return a + b + c


# [패킹]
nums = [1, 2, 3, 4, 5]
nums2 = (1, 2, 3, 4, 5)
print(nums, nums2)

# 언패킹
a, b, c, d, e = nums
print(a, c, d)

# 언패킹 하고 남은 값은 *(astrisk/astral)를 이용해서 리스트에 담을 수 있다...
a, b, *c = nums
print(a, b, c)      # 짱 신기

a, *b, c = nums
print(a, b, c)      # 짱 신기


def getSum(*a):         # 매개변수 개수를 지정하지 않을 때
    print(type(a))      # tuple !!!
    return a[0] + a[1] + a[2]

ret = getSum(3, 5, 1)
print(ret)


def print_info(**args):     # 정해지지 않은 개수의 키워드 인자를 매개변수로 받는다
    print(args)             # {'kevin': 1, 'bob': 2, 'john': 3}
    print(type(args))       # <class 'dict'>
    for i,j in args.items():
        print(i,j)          # dictionary의 key, value를 반환하는 매서드

print_info(kevin=1, bob=2, john=3)


# [변수 scope]
# 지역변수 ~~~ 전역변수
def abc():
    aa=3
    bb=5
    print(aa,bb)

abc()
# print(aa, bb)   # NameError: name 'aa' is not defined

# -------------# -------------------

aa = 6
def abc():
    aa=3        # '함수 안의 지역변수'는 '함수 밖의 전역변수'와 이름이 같더라도 다른 변수임. ㅋㅅㅋ
    bb=5
    print(aa,bb)

abc()
print(aa)   # 함수 안의 지역변수인 aa가 아니라 전역변수를 받는다.

# -------------# -------------------

aa = 6
def abc():
    global aa
    aa=3        # aa가 전역변수가 되어버림. 함수 밖에서 정의된 aa가 바뀐다.
    bb=5
    print(aa,bb)

abc()
print(aa)

# -------------# -------------------

def kfc():
    global aa, bb
    print(aa,bb)
    aa+=1
    bb+=1
    print(aa,bb)

def test():
    global aa, bb
    aa=3
    bb=5
    print(aa,bb)

test()      # 3 5
kfc()       # 4 6

# [내장함수]
# map - list나 tuple과 같이 순회 가능한 데이터 값에 함수를 일괄적으로 적용
#     - 적용 후 map이라는 객체를 반환한다.
num=['1', '2', '3']
lst=map(int,num)
print(list(lst))

# zip - 순회 가능 한 객체를 인자로 받고
#     - 각각의 값을 잘라서! "tuple"을 원소로 하는 객체 반환
a = '12345'
b = 'qwert'
c = 'asdfg'

ret = zip(a, b, c)
print(ret)
print(list(ret))    # 짱 신기

# -------------------# -------------------
for i in zip(a, b, c):
    print(list(i))    # 짱 신기

# -------------------# -------------------
arr=[[1,2,3],[4,5,6],[7,8,9]]
print(arr)

for i in zip(arr[0], arr[1], arr[2]):
    print(list(i))