'''
# 1. 출력
print( "Hello World" )
print( 'Mary\'s cosmetic' )
print( "신씨가 소리질렀다. \"도둑이야\"" )
print( "C:\\Windows" )
print( "안녕하세요.\n만나서\t\t반갑습니다. " )
# \n은 줄바꿈, \t는 탭
print( "오늘은","일요일" )
#오늘은 일요일
print( "naver","kakao","sk","samsung", sep=";" )
print( "naver","kakao","sk","samsung", sep="/" )
print( "first", end="" ); print("second")
print( 5 / 3 )


print("-")



# 2. 변수
삼성전자 = 50000
총평가금액 = 삼성전자 * 10
print( 총평가금액 )

s = "hello"
t = "python"
print( f"{s}! {t}" )

num = 2 + 2 * 3
print( num )

a = "132"
print( type(a) )

num_str = "720"
print( int(num_str) )

num = 100
print( str(num) )

num = "15.79"
print( float(num) )

year = "2020"
print( int(year), int(year)-1, int(year)-2 )

air = 48584
month = 36
print ( f"총 금액: {air * month} 원" )



#Q. 두 수와 연산자를 입력받고, 사칙연산 결과를 출력하는 프로그램
# (덧셈, 뺄셈, 곱셈, 나눗셈만 실행)

n1 = int(input("수 입력: "))
n2 = int(input("수 입력: "))
Operator = input("연산 기호: ")

if Operator == '+':
    print( f"{n1} + {n2} = {n1 + n2}" )
elif Operator == '-':
    print( f"{n1} - {n2} = {n1 - n2}" )
elif Operator == '*':
    print( f"{n1} * {n2} = {n1 * n2}" )
elif Operator == '/':
    print( f"{n1} / {n2} = {n1 / n2}" )
else:
    print( "사칙연산만 가능합니다" ) 
'''



print( "-" )



# 3. 분기문
# n = input(">> ")
# print( n * 2 )


# n = int(input("입력: "))
# print( n + 10 )


# n = int(input("입력: "))

# if n % 2 == 0:
#     print( "짝수" )
# else:
#     print( "홀수" )


# n = int(input("입력: "))
# n += 20

# if n > 255:
#     print( 255 )
# else:
#     print( n )


# n = int(input("입력: "))
# n -= 20

# if n < 0:
#     print( 0 )
# if n >= 225:
#     print( 225 )
# else:
#     print( n )


# n = input("현재 시간: ")

# if n[-2:] == '00':
#     print( "정각" )
# else:
#     print( "정각이 아닙니다" )


# F = input("좋아하는 과일은? ")
# fruit = ['사과', '포도', '홍시']

# if F in fruit:
#     print( "정답입니다" )
# else:
#     print( "오답입니다" )


# 남규님 (내가 푼 거 틀림ㅋㅋ 다시 풀어 보자)
# slice01 = int(input("조각 수: "))
# n = int(input("사람 수: "))

# if 2 <= slice01 and slice01 <= 10:
#     if 1 <= n and n <= 100:
#         print( f"{n} 명의 사람이 {slice01} 조각씩 잘라 줄 때, 최소 한 조각 이상 피자를 먹으려면 최소 {int(n / slice01)} 판의 피자를 시켜야 합니다")
#     else:
#         print( "1명 이상 100명 이하의 사람이 있어야 합니다")
# else:
#     print( "두 조각에서 열 조각까지만 가능합니다" )


# answer =0
# slice01 = int(input('피자당 잘라주는 조각수 :'))
# n = int(input('피자를 먹는 사람수:'))
# if n % slice01 ==0 :
#     answer = n//slice01
# else :  # n % slice01 !=0
#     answer = n//slice01 + 1 # (몫+1) 판을 주문하면됨.
# print(f'{n}명의 사람이 {slice01}조각씩 잘라줄때, 최소 한조각 이상 피자를 먹으려면 최소 {answer}판의 피자를 시켜야합니다.')



# 진수님
# age = int(input("고객 나이: "))
# N = int(input("티켓 개수: "))
# ticket = 13000

# if age >= 0 and age <= 6:
#     print( "구매 불가!!!" )
# elif age >= 7 and age <= 9:
#     ticket = 5000
#     print( f"금액: {N * ticket} 원" )
# elif age >= 10 and age <= 19:
#     ticket = ticket - (ticket * 0.2)
#     print( f"금액: {int(N * ticket)} 원" )
# elif age >= 20 and age <= 29:
#     ticket = ticket - (ticket * 0.1)
#     print( f"금액: {int(N * ticket)} 원" )    
# elif age >= 60:
#     ticket = ticket - (ticket * 0.4)
#     print( f"금액: {int(N * ticket)} 원" )
# else:
#    print( f"금액: {N * ticket} 원" ) 



# num = input("번호 입력: ")

# if num[:3] == '011':
#     print( "통신사: SKT" )
# elif num[:3] == '016':
#     print( "통신사: KT" )
# elif num[:3] == '019':
#     print( "통신사: LGU" )
# elif num[:3] == '010':
#     print( "통신사: 알수없음" )


# age = int(input("나이 입력: "))

# if age < 8:
#     money = 450
# elif 8 <= age <= 19:
#     money = 720
# elif age >= 20:
#     money = 1250

# print( f"요금은 {money}원" )


# born = int(input("출생년도 입력: "))

# if born % 12 == 0:
#     print( "원숭이띠" )
# elif born % 12 == 1:
#     print( "닭띠" )
# elif born % 12 == 2:
#     print( "개띠" )
# elif born % 12 == 3:
#     print( "돼지띠" )
# elif born % 12 == 4:
#     print( "쥐띠" )
# elif born % 12 == 5:
#     print( "소띠" )
# elif born % 12 == 6:
#     print( "범띠" )
# elif born % 12 == 7:
#     print( "토끼띠" )
# elif born % 12 == 8:
#     print( "용띠" )
# elif born % 12 == 9:
#     print( "뱀띠" )
# elif born % 12 == 10:
#     print( "말띠" )
# elif born % 12 == 11:
#     print( "양띠" )


# 2x1   3x1 4x1
# 2x2   3x2 4x2

# #Q. 입력받은 값까지의 구구단 출력
# N = int(input("입력: "))
# for i in range(1, 10):
#     for k in range(2, N+1):
#         print( f"{k} x {i} = {k * i}", end="\t" )
#     print()

'''
#Q. 1에서 N까지 3의 배수와 5의 배수의 개수와 총 합을 구하세요. 단, 15의 배수는 제외하세요.

N = int(input("수 입력: "))

li_3 = cnt_3 = cnt_5 = sum_3 = sum_5 = 0

for i in range(1, N+1):
    if i % 15 != 0:
        if i % 3 == 0:
            cnt_3 += 1
            sum_3 += i  
        if i % 5 == 0:
            cnt_5 += 1
            sum_5 += i
print( f"3의 배수의 개수: {cnt_3}, 합: {sum_3}" )
print( f"5의 배수의 개수: {cnt_5}, 합: {sum_5}" )


cnt = 0
for i in range(1, 32):
    if i % 7 == 6:
        print( i, end="일, " )
        cnt += 1
print( f"총 {cnt} 번 있다" )



# 진수님 문제
price = 3000
beer = int(input("구매 개수: "))
a_price = price * beer

cnt = 0
dc = 0
for i in range(1, beer+1):
    if i % 4 == 0:
        cnt += 1
        dc = cnt * price

print( f"맥주 {beer}개의 총 금액은 {a_price - dc}원, 할인 금액은 {dc} 원" )



N = int(input("단 입력: "))
for i in range(1, 10):
    for k in range(2, N+1):
        print( f"{k} x {i} = {i * k}" )


N = int(input("입력: "))
for i in range(1, N+1):
    print( "*" * i )
'''

# N = int(input("입력: "))
# a = N // 1000
# b = N // 100 % 10
# c = N // 10 % 10
# d = N % 10

# answer = 0
# if N % 2 == 0:
#     if a % 2 == 0:
#         answer += a
#     if b % 2 == 0:
#         answer += b
#     if c % 2 == 0:
#         answer += c
#     if d % 2 == 0:
#         answer += d
#     print(answer)

# else:
#     if a % 2 == 1:
#         answer = a
#     if b % 2 == 1:
#         answer += b
#     if c % 2 == 1:
#         answer += c
#     if d % 2 == 1:
#         answer += d
#     print(answer)
    

# N = int(input("입력: "))

# answer = 0
# str_ = str(N)
# if int(N) % 2 == 0:
#     for i in str_:
#         if int(i) % 2 == 0:
#             answer += int(i)
# else:
#     for i in str_:
#         if int(i) % 2 != 0:
#             answer += int(i)
# print( answer )



