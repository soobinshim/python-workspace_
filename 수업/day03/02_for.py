'''
반복문
- 어떤 내용을 반복하고자 하는 경우
- 규칙적으로 값이 변경될 때
for 변수 in range(초기값, 비교값, 증감값):
    종속 문장
'''

num = 0
num += 1
print( num )
num += 1
print( num )
num += 1
print( num )
num += 1
print( num )
num += 1
print( num )
num += 1
print( num )


print( "-" )


for i in range(0,11,1): # (i=0, i<11, i=i+1)
    print( i )
print( "다음 문장 실행" )


print( "-" )


for i in range(1,11,1): # (i=1, i<11, i=i+1)
    print( "----- for 시작" )
    if i % 2 == 0:
        print( f"i = {i}" )
    print( "for 종료 -----" )
print( "다음 문장 실행" )


print( "-" )


for i in range(1, 11, 2):
    print( i )


print( "-" )


print( "안녕", end="" ) # end="" 끝값을 엔터 대신에 "" 로 변경
# print()
print( "하세" )
print( "요" )

for i in range(1, 11, 1):
    print( i, end=" " )


print( "-" * 100 )


#Q1.
print( "#Q1. ")
print( "1) 1 ~ 10까지의 합" )
sum_ = 0
for i in range(1, 11, 1):
    sum_ += i
print( sum_ )

print( "-" )

print( "2)" )
for i in range(1, 31, 1):
    print( i, end="\t" )
    if i % 5 == 0:
        print()
    

print( "-" * 100 )


#Q2.
print( "#Q2. 수를 입력받아 1 ~ 입력받은 수까지 짝수의 합과 홀수의 합을 구하시오" )
n = int(input("입력: "))
sum1 = 0
sum2 = 0
for i in range(1, n+1, 1):
    if i % 2 == 0:
        sum1 += i
    else:
        sum2 += i
print ( f"홀수의 합은 {sum2}, 짝수의 합은 {sum1}" )


print( "-" * 100 )


for i in range(0, 10):
    print( i, end=", " )
print()

print ( "-" )

for i in range(10):
    print( i, end=", " )
print()


print( "-" * 100 )


#Q3.
print( "#Q3. 두 수를 입력받아 입력받은 두 수의 범위 안의 합을 구하시오" )
N1 = int(input("수 입력: "))
N2 = int(input("수 입력: "))
sum_ = 0
for i in range(N1, N2+1, 1):
    sum_ += i
for i in range(N2, N1+1, 1):
    sum_ += i
print( f"합: {sum_}" )

print( "-" )
N1 = int(input("입력: "))
N2 = int(input("입력: "))
if N1 > N2:
    max_ = N1
    min_ = N2
else:
    max_ = N2
    min_ = N1

sum_ = 0
for i in range(min_, max_+1):
    sum_ += i
print( f"범위안의 합: {sum_}" )


print( "-" * 100 )


st = "Hello Python"
for i in st:
    print( i )


print( "-" * 100 )


st = "It is a fun Python class"
a_cnt = 0
s_cnt = 0
cnt = 0
for i in st:
    if i == 'a':
        a_cnt += 1
    if i == 's':
        s_cnt += 1
    cnt += 1
print( f"a의 개수: {a_cnt}\ns의 개수: {s_cnt}\n총 개수: {cnt}" )


