'''
변수
- 무언가(데이터)를 저장하기 위한 공간

변수 이름 작성 규칙
- 의미를 부여해서 만든다
- 이름은 영어로 만든다
- 보통 3~10자 이내로 만든다 number -> num
- 키워드는 사용하면 안 된다
'''
import keyword
print( keyword.kwlist )
# 'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield'


num = 100
print( num )
print( 100 )

age = 20
print( f"나의 나이는 {age} 살입니다" )
print( f"만으로는 {age - 1} 살입니다" )
print( f"내년에는 {age + 1} 살입니다" ) 

n = 5
print( f"변경 전 n:", n )
n = n + 10
print( f"변경 후 n: {n}" )

n1 = 5
n2 = 10
sum_ = n1 + n2
print( f"{n1} + {n2} = {sum_}" )


print( "-" * 100 )


#Q1.
print( "#Q1." )
n1 = 10
n2 = 20
sum_ = n1 + n2
print("num1(", n1, ") +", "num2(", n2, ") =", sum_ )
print( f"num1({n1}) + num2({n2}) = {sum_}" )
print( "num1({}) + num2({}) = {}".format(n1, n2, sum_) )


print( "-" * 100 )


flt = 123.456
print( "flt :", flt )
print( "round(flt) :", round(flt) )
print( "round(flt, 1) :", round(flt, 1) )
print( "round(flt, 2) :", round(flt, 2) )


print( "-" * 100 )


#Q2.
print( "#Q2." )
print( "1) 파이썬, C언어, Java 3과목의 점수를 저장하고 합계와 평균을 구하는 프로그램" )
p = 100
c = 90
j = 76
sum_ = p + c + j
avg_ = round( (p + c + j) / 3, 2 )
print( f"합: {sum_} 점\n평균: {avg_} 점" )

print( "-" )

print( "2) 놀이공원을 가기 위해 11개의 지하철역을 지났다. 출발역에서 도착역까지 37분 걸렸다면, 한 역을 지나는 데 걸리는 시간은 얼마인가?" )
subway = 11
time = 37
st = round( (time / subway), 2 )
print( f"한 역을 지나는 데 걸리는 시간: {st} 분" )

print( "-" )

print( "3) 호텔 한 층의 높이는 260cm 총 14 개의 층을 쓰고 있으며 1 층은 500.23cm라면 이 건물의 높이는 총 몇 m인가?" )
height = 260
first = 500.23
floor = 14
sum = round( ((height * (floor-1)) + first) / 100, 3 )
print( f"총 높이: {sum}m" )
