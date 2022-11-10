n1 = 9
n2 = 2
print( f"{n1} + {n2} = {n1 + n2}" )     # 더하기
print( f"{n1} * {n2} = {n1 * n2}" )     # 곱하기
print( f"{n1} / {n2} = {n1 / n2}" )     # 나누기
print( f"{n1} // {n2} = {n1 // n2}" )   # 몫
print( f"{n1} % {n2} = {n1 % n2}" )     # 나머지
print( f"{n1} ** {n2} = {n1 ** n2}" )   # 승 수

print( "-" )
'''
관계 연산자
>, <, <=, >=, ==, !=
- 결과적으로 참(True)인지 거짓(False)인지 판단
- 이항 연산자
'''

n1 = 3.1
n2 = 3
print( "n1 >= n2 :", (n1 >= n2) )
print( "n1 >= n2 :", (n1 < n2) )
print( "n1 >= n2 :", (n1 == n2) )
print( "n1 >= n2 :", (n1 != n2) )

print( "-" )
'''
복합 연산자
num = 10;
num(110) = num + 100
num += 100
num *= 100, num %= 100, ...
'''

n1 = n2 = 5
n1 += 1     # n1 = n1 + 1
print( n1 ) # 6
n1 -= 1     # n1 = n1 - 1
print( n1 ) # 5
n1 *= n2    # n1 = n1 * n2
print( n1 ) # 25
n1 //= n2   # n1 = n1 // n2
print( n1 ) # 5
n1 %= n2    # n1 = n1 % n2
print( n1 ) # 0

n1 = 5
n2 = 3
n1 **= n2       # n1 = n1 ** n2 # n1 = 125
n1 -= 2         # n1 = n1 - 2   # n1 = 123
print( n1 / 4 ) # 123 / 4       # 30.75
print( n1 // 4 )# 123 // 4      # 30
print( n1 % 4 ) # 123 % 4       # 3

print( "-" )
'''
논리 연산자
- 여러 개의 식을 묶어서 연산한다
num = 10
- and   : 조건 모두가 참일 때 결과는 참 / 하나라도 거짓이면 결과는 거짓
            (num > 10) and (num % 2 == 0) : True
- or    : 조건 중 하나라도 참이면 결과는 참
- not   : 결과를 반전시켜 준다
'''

print( True and True )  # True
print( False and True ) # False
print( True and False ) # False
print( False and False )# False

n1 = 12
print( "n1 > 10 :", n1 > 10 )
print( "n1 % 2 :", n1 % 2 )
print( "0 == 0 :", 0 == 0 )
print( n1 > 10 and n1 % 2 == 0 )

print( True or True )  # True
print( False or True ) # True
print( True or False ) # True
print( False or False )# False

print( "not True :", not True )
print( "n1 > 10 :", not n1 > 10 )
print( "not n1 > 10 :", not n1 > 10 )