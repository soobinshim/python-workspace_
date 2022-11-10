'''
제어문
- 프로그램의 흐름을 제어한다
- if, for, while, break, continue
    if 조건식:
        종속 문장
    다음 문장
'''

print( "1. 쉬운 게임" )
print( "2. 어려운 게임" )
print( "3. 종료" )

num = int(input(">>> "))

if num == 1:
    print( "쉬운 게임 실행!!!" )
if num == 2:
    print( "어려운 게임 실행!!!" )
if num == 3:
    print( "게임 종료" )
    

print( "-" )


n1 = 15
n2 = 10

if n1 > n2:
    print( f"{n1}이(가) {n2}보다 크다" )


print( "-" )


print( "=== 짝수 판단 ===" )
n1 = int(input("수 입력: "))

if n1 % 2 == 0:
    print( f"{n1} 짝수이다" )
    print( f"{n1}은(는) 2의 배수이다" )
    print( "종속 문장들 실행" )
print( "다음 문장 실행" )
print( "다음 문장 실행" )


print( "-" * 100 )


#Q1.
print( "#Q1. 절대값을 구하는 프로그램" )
num = int(input("수 입력: "))

if num > 0:
    print( f"{num}의 절대값은 {num}" )
if num < 0:
    print( f"{num}의 절대값은 {-num}" )


print( "-" * 100 )


#Q2.
print( "#Q2. 세 수를 입력받아 가장 큰 수 출력" )
num1 = int(input("수 입력: "))
num2 = int(input("수 입력: "))
num3 = int(input("수 입력: "))

if num1 > num2 and num1 > num3:
    print( f"{num1}이(가) 가장 큰 수" )
if num2 > num1 and num2 > num3:
    print( f"{num2}이(가) 가장 큰 수" )
if num3 > num1 and num3 > num2:
    print( f"{num3}이(가) 가장 큰 수" )

