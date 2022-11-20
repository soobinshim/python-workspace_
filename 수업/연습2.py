# def func():
#     pass

# def func():
#     '''
#     함수 기능 설명
#     함수 결과 예제
#     '''
#     pass

# func()


# def funcHello():
#     print( "Hello Python" )

# def funcVersion():
#     print( "Title: Python Programming Basic\nVersion: 1.0 Ver" )

# funcHello()
# funcVersion()


# def funcInt():
#     return 10

# var = funcInt() + 10
# print( var )


# def func():
#     #return (1,2,3)
#     return [1,2,3]

# var = func()
# print(var[0], var[1], var[2])


# def func():
#     return {'a':1, 'b':2}

# var = func()
# print(var['a'], var['b'])


# def func(arg):
#     print( arg )

# func(1)


# def func(arg1, arg2):
#     print( arg1, arg2 )

# func('a', 'b')


# def func(arg):
#     print( arg + 10 )

# func(10)

# def func(arg1, arg2):
#     print( arg1 + arg2 )

# func(10, 40)


# def func(num = 1):
#     print(num)

# func(5)
# func()


# def func(num = 1):
#     print( num * 4 )

# func()
# func(4)

# def func(num1, num2=2):
#     print( num1, num2 )

# func(5)
# func(5, 10)


# def func(num1, num2):
#     print( num1, num2 )

# func(3, 5)
# func(num2=3, num1=1)


# def func(n1, n2=1, n3=2):
#     print( n1, n2, n3 )

# func(5,2,4)
# func(5, n3=4)


# def func(num, *nums):
#     print(num, nums)

# func(1,2,3,4,5)


# def func(num, *nums):     # *nums 튜플 형태
#     print( num, nums )

# func(1,2,3,4,5,6)


# def func(num, **nums):      # **nums 사전형
#     print(num, nums)

# func(1, key1=10, key2='a')


# def func(num, **nums):
#     print( num, nums )

# func(1, n1=1, n2=2, n3='a', n4='c')


# a = 1
# b = 2
# def func():
#     print( a,b )

# func()
# print( a, b )


# def func():
#     a = 1
#     b = 2
#     print( a, b )

# func()
# #print( a, b )  # 지역 변수 사용 중이므로 출력 x


# a, b = 1, 2
# def func():
#     a, b = 3, 4
#     print( a, b )

# func()
# print( a, b )


# def programInfo():
#     res = "Version: 1.0\n"
#     res = res + "Update Date: 2017-01-01\n"
#     res = res + "Author: Project Python"
#     return res

# print( programInfo() )


# def pyMax(*nums):
#     mx = nums[0]
#     for i in nums[1:]:
#         if mx < i:
#             mx = i
#     return mx

# print( pyMax(24,193,258,210,23,140) )

# def pyMin(*nums):
#     mn = nums[0]
#     for i in nums[1:]:
#         if mn > i:
#             mn = i
#     return mn

# print( pyMin(12,59,140,23,104,6,1340) )

# from random import random

# # 0~N, M~N
# def myrandom(min, max=0):
#     if max == 0:
#         min, max = max, min
#     return int(random() * (max-min)) + min

# print( myrandom(5) )
# print( myrandom(1,5) )




'''
#1).입력한 데이터가 3의 배수인 경우 출력 하시오.
N = int(input(" 수 입력: "))

if N % 3 == 0:
    print( f"{N}은 3의 배수" )



#2).수를 입력 받아 짝,홀수를 구분하여 출력 하시오.
N = int(input("수 입력: "))

if N % 2 == 0:
    print( f"{N}은 짝수" )
else:
    print( f"{N}은 홀수" )



#3).두수를 입력 받아 큰 수를 출력 하시오.
N1 = int(input("수 입력: "))
N2 = int(input("수 입력: "))

if N1 > N2:
    print( f"더 큰 수는 {N1}" )
elif N2 > N1:
    print( f"더 큰 수는 {N2}" )
else:
    print( "두 수가 같습니다" )



#4).수를 입력받아 절대값을 구하는 프로그램을 작성 하시오.
N = int(input("수 입력: "))

if N < 0:
    print( f"{N}의 절대값은 {-N}" )
else:
    print( f"{N}의 절대값은 {N}" )
'''


'''
#1).날짜를 입력 받아 요일을 구하시오.
#단, 1일은 무조건 월요일이다. 7일은 일요일, 8일은 다시 월요일
#어떤 값을 입력 받던 요일이 정확히 출력 되게 만드시오.
N = int(input("요일 입력: "))
if N % 7 == 0:
    print( f"{N}일은 일요일" )
elif N % 7 == 1:
    print( f"{N}일은 월요일" )
elif N % 7 == 2:
    print( f"{N}일은 화요일" )
elif N % 7 == 3:
    print( f"{N}일은 수요일" )
elif N % 7 == 4:
    print( f"{N}일은 목요일" )
elif N % 7 == 5:
    print( f"{N}일은 금요일" )
elif N % 7 == 6:
    print( f"{N}일은 토요일" )



#2).세수를 입력 받아 큰 수를 출력 하시오.
N1 = int(input("수 입력: "))
N2 = int(input("수 입력: "))
N3 = int(input("수 입력: "))

if N1 > N2 and N1 > N3:
    print( f"가장 큰 수는 {N1}" )
elif N2 > N1 and N2 > N3:
    print( f"가장 큰 수는 {N2}" )
elif N3 > N1 and N3 > N2:
    print( f"가장 큰 수는 {N3}" )



#3).두수를 입력 받아 큰 수가 짝수이면 출력 하시오.
N1 = int(input("수 입력: "))
N2 = int(input("수 입력: "))

if N1 > N2 and N1 % 2 == 0:
    print( f"{N1}은 큰 수이며 짝수이다" )
elif N2 > N1 and N2 % 2 == 0:
    print( f"{N2}은 큰 수이며 짝수이다" )



#4).두수를 입력 받아 합이 짝수이고 3의 배수인 수를 출력 하시오.
N1 = int(input("수 입력: "))
N2 = int(input("수 입력: "))
sum_ = N1 + N2

if sum_ % 2 == 0 and sum_ % 3 == 0:
    print( f"{N1} + {N2} = {sum_}, 짝수이며 3의 배수이다" )
'''


'''
#1).1~100 까지의 총 합을 구한다. 단, 3의 배수는 제외하고 3의 배수이며 5의 배수는 제외하지 않는 조건이다.
sum1 = 0
sum2 = 0
for i in range(1, 101):
    sum1 += i

    if i % 3 == 0:
        if i % 15 != 0:
            sum2 += i

print( f"총 합: {sum1 - sum2}" )



#2).두 수를 입력 받아 입력 받은 두 수의 범위 안의 합을 구하시오
#1입력, 10입력 => 55
#10입력,1입력 => 55
N1 = int(input("수 입력: "))
N2 = int(input("수 입력: "))
min_ = 0
max_ = 0
sum_ = 0

if N1 < N2:
    min_ = N1
    max_ = N2
else:
    min_ = N2
    max_ = N1

for i in range(min_, max_+1):
    sum_ += i
print( sum_ )
        


#3).첫날에 10원을 예금하고, 다음날에는 전날의 2배를 예금하는 방식으로 한달(30일) 이 되는 날
# 입금해야 하는 금액은 얼마인지 구하시오
#(첫날 10, 둘 째날 20 , 셋 째날 40 . . .무조건 2배씩 증가되는 값이다)

for i in range(1, 31):
    if i == 1:
        won = 10
    else:
        won = won * 2
print( f"입금 금액: {won} 원" )



#4) 아래와 같이 출력되게 2중 for문을 이용하여 출력하시오
#상위포문 0 일 때 하위 포문 : 0 0 0 0 0
#상위포문 1 일 때 하위 포문 : 0 1 2 3 4
#상위포문 2 일 때 하위 포문 : 0 2 4 6 8
#상위포문 3 일 때 하위 포문 : 0 3 6 9 12
#상위포문 4 일 때 하위 포문 : 0 4 8 12 16
for i in range(0, 5):
    print( f"상위 포문 {i}일 때 하위 포문: ", end=" " )
    for j in range(0, 5):
        print( i*j, end=" " )
    print()
'''


'''
#랜덤과 set을 이용하여 로또 프로그램을 만드시오
import random

s = set()
while len(s) < 6:
    s.add(random.randrange(1, 46))
print( s )
'''




# 다음 내용을 lambda와 map을 이용하여 아래와 같이 표현하시오
#day = { '날짜' : ['2018.01.01.','2019.02.02','2020.03.03'] }

#2018년 01월 01일
#2019년 02월 02일
#2020년 03월 03일













