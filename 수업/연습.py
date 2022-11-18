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



# N = int(input("입력: "))
# cnt_3 = cnt_5 = sum_3 = sum_5 = 0
# for i in range(1, N+1):
#     if i % 15 != 0:
#         if i % 3 == 0:
#             cnt_3 += 1
#             sum_3 += i
#         if i % 5 == 0:
#             cnt_5 += 1
#             sum_5 += i
# print( f"3의 배수의 개수: {cnt_3}, 합: {sum_3}" )
# print( f"5의 배수의 개수: {cnt_5}, 합: {sum_5}" )


# N = int(input("입력: "))
# i = cnt_3 = cnt_5 = sum_3 = sum_5 = 0
# while i <= N: 
#     i += 1  
#     if i % 15 != 0:
#         if i % 3 == 0:
#             cnt_3 += 1
#             sum_3 += i
#         if i % 5 == 0:
#             cnt_5 += 1
#             sum_5 += i
# print( f"3의 배수의 개수: {cnt_3}, 합: {sum_3}" )
# print( f"5의 배수의 개수: {cnt_5}, 합: {sum_5}" )




# N = int(input("입력: "))
# cnt = 0
# for i in range(1, N+1):
#     for k in range(i):
#         print(i, end="")
#         cnt += 1
# print( f"\n총 길이: {cnt}" )


# N = int(input("입력: "))
# for i in range(1, 10):
#     for k in range(2, N+1):
#         print( f"{k} x {i} = {i * k}", end="\t" )
#     print()


# R_ = 1
# for i in range(1, 11, 1):
#     R_ = i * R_
# print( R_ )



# f = 10
# sum_ = 0
# for i in range(1, 30):
#     sum_ += (f * 2)
# print( f + sum_ )

# print( 20*29 + 10 )



# N1 = int(input("양꼬치 몇 인분? "))
# N2 = int(input("음료수 몇 개? "))
# kko = 12000 * N1
# drink = 2000 * N2

# for i in range(1, N1+1):
#     cnt = 0
#     if i % 10 == 0:
#         cnt += 1
#         drink = drink - (cnt * 2000)

# print( f"양꼬치 {N1} 인분({kko}원) 음료수 {N2}개({drink}원)는 총 {kko + drink} 원" )


# for i in range(0, 5):
#     print( f"상위포문 {i}일 때 하위 포문: ", end="" )
#     for j in range(0, 5):
#         print( i * j, end=" " )
#     print()


# for i in range(0, 5):
#     for k in range(1, 6):
#         print( (i * 5) + k, end="\t" )
#     print()


# num = int(input("정수값: "))
# 결과 = ""
# while True:
#     나머지 = num % 2
#     num = num // 2
#     결과 = str(나머지) + 결과
#     if num == 0:
#         print(결과)
#         break

# ls = []
# for i in range(5):
#     N = int(input(f"{i}. 수 입력: "))
#     ls.append(N)

# avr = sum(ls) / len(ls)

# if i < avr:
#     print( f"{i}는 평균 미만" )


# ls = []
# N = int(input("수 입력: "))
# for i in range(1, N+1):
#     if N % i == 0:
#         ls.append(i)
# print( ls )



# ls = []
# N = int(input("수 입력: "))
# for i in range(1, N+1):
#     if N % i == 0:
#         ls.append(i)
# print( f"{N}의 약수: {ls}" )


# N = int(input("수 입력: "))
# for i in range(2, N+1):
#     ls = []
#     for k in range(2, i+1):
#         if i % k == 0:
#             ls.append(k)
#     print( f"{k}의 약수 {ls}" )
# print()


# Q8. 수(A)를 입력받고 소수인지 판별하는 프로그램
# 소수 : 약수로 1과 자기 자신만 갖는 수 (1,3,5,7,11,13...)


# price = ['20180728', 100, 130, 140, 150, 160, 170]
# print( price[1:])

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print( nums[::2] )
# print( nums[1::2] )
# print( nums[::-1])

# interest = ['삼성전자', 'LG전자', 'Naver']
# print( interest[0], interest[2] )

# interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# print( interest[0:4])

# st = "125,424,000"
# st = int(st.replace(",", ""))
# #st = int(st)
# print( st )

# #Q. 아래 문자열을 콤마 제거 후 정수 타입으로 변환하세요
# st = '127,000,254'
# #(st 출력 시 127000254가 출력되도록)


# st = st.replace(",","")
# st = int(st)
# print( st, type(st) )

# st = 'python'
# print( st[0], st[2])

# string = "홀짝홀짝홀짝"
# print( string[::2] )

# string = "PYTHON"
# print( string[::-1] )

# phone_number = "010-1111-2222"
# phone_number = phone_number.replace("-"," ")
# print( phone_number )

# phone_number = phone_number.replace(" ", "")
# print( phone_number )


# st1 = input("단어 입력: ")

# while True:
#     st2 = input(f"{st1}: ")
    
#     if st1[-1] == st2[0]:
#         st1 = st2
#     else:
#         print( "땡" )
#         break


# ls = ['20181127', '19860303', '20000324', '19750119', '19900407', '19850511', '20090517', '19811214', '20120125', '19920308', '20040610', '19990310', '20171126', '20160727', '19751006', '19920823', '20060103', '20171208', '19990222', '19731206', '19960824', '19970902', '19780714', '19901002', '19970224', '20091107', '19730209', '19890601', '19951003', '20051022', '19770520', '20000206', '19711221', '19820526', '20080413', '20200104', '19780204', '20030524', '20040509', '19800225', '19820327', '20130610', '19880426', '19880421', '19850101', '20011205', '19940326', '20200104', '19750823', '19701226', '20190626', '20150819', '19720626', '19890910', '20081223', '19831028', '19910406', '20160118', '20150823', '20090925', '19970812', '19800123', '20151108', '20020109', '19820414']
# cnt = 0
# for i in ls:
#     if i[:4] == '1988':
#         cnt += 1
# print( cnt, "명" )


# ls = ['4910000원', '1544000원', '2536000원', '3843000원', '144000원', '2619000원', '3835000원', '2165000원', '3706000원', '2963000원', '2292000원', '3020000원', '757000원', '4777000원', '2746000원', '1207000원', '1857000원', '2317000원', '339000원', '4815000원', '1818000원', '2527000원', '3814000원', '1408000원', '2516000원', '3562000원', '196000원', '3306000원', '334000원', '3883000원', '4146000원', '744000원', '4278000원', '1005000원', '3386000원', '883000원', '2138000원', '4705000원', '1484000원', '4550000원', '3068000원', '1349000원', '4424000원', '609000원', '4356000원', '3225000원', '1540000원', '4515000원', '4068000원', '41000원', '67000원', '1006000원', '3722000원', '3374000원']
# sum = 0
# for i in ls:
#     sum += int(i[:-1])
# print( sum )


# id_ls = []
# pw_ls = []

# while True:
#     user_id = input("아이디 입력: ")

#     if len(user_id) < 10:
#         print( "아이디는 10자리 이상 입력해 주세요" )
#     else:
#         break

# while True:
#     user_pw = input("비밀번호 입력: ")
#     if 8 <= len(user_pw) <= 16:
#         if user_id not in user_pw:
#             cnt = 0
#             for s in '~!@#$%^&*_?':
#                 if s in user_pw:
#                     cnt = 1
#                     break
#             if cnt == 0:
#                 print( "비밀번호에는 특수문자가 한 개 이상 포함되어야 합니다" )
#             else:
#                 print( "회원가입 완료" )
#                 break
#         else:
#             print( "아이디가 패스워드에 포함되어 있으면 안 됩니다" )
#     else:
#         print( "비밀번호는 8자리 이상 16자리 이하로 입력해 주세요" )


#num = {}

#while True:
#    name = input("이름 입력: ")
    
#    if not name:
#        break;
    
#    phone = int(input("전화번호 입력: "))
#    num[name] = phone
        
#while True:
#    name2 = input("검색할 이름: ")
#    print( f"{name2}의 전화번호는 {num[name2]}입니다." )


'''
def Myinput():
    num1 = int(input("수 입력: "))
    num2 = int(input("수 입력: "))
    return num1, num2

def Main(n1, n2):
    if n1 > n2:
        print( n1 - n2 )
    else:
        print( n2 - n1 )

n1, n2 = Myinput()
Main(n1, n2)


#Q. 입력받은 수의 약수를 구해주는 함수
def Myinput():
    n = int(input("수 입력: "))
    return n

def Test(n):
    li = []
    for i in range(1, n+1):
        if n % i == 0:
            li.append(i)
    return li

n = Myinput()       
print(Test(n))
'''


