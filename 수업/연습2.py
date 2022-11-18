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



