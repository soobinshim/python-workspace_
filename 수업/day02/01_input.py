num1 = input("수 입력: ")
print( "입력값:", num1)


print( "-" * 100 )


#Q1.
print( "#Q1." )
name = input("이름 입력: ")
age = input("나이 입력: ")
print( f"{name} 님의 나이는 {age} 살입니다" )


print( "-" * 100 )


print( "두 수의 합을 구해 줍니다" )
n1 = input("수 입력: ")
n2 = input("수 입력: ")
s = n1 + n2
print( "두 수 합:", s ) # 문자열이기 때문에 연산은 되지 않음


print( "-" * 100 )


#Q2.
print( "#Q2." )
print( "두 수의 합을 구해 줍니다" )
n1 = input("첫 번째 수 입력: ")
n2 = input("두 번째 수 입력: ")
s = int(n1) + int(n2)
print( f"두 수의 합 {n1} + {n2} = {s}" )

print( "-" )

print( "두 수의 합을 구해 줍니다" )
n1 = int(input("첫 번째 수 입력: "))
n2 = int(input("두 번째 수 입력: "))
s = n1 + n2
print( f"두 수의 합 {n1} + {n2} = {s}" )


print( "-" * 100 )


#Q3.
print( "#Q3." )
print( "1) 올해 년도와 태어난 년도를 구하여 나이를 계산하는 프로그램을 코딩하시오" )
y = int(input("올해의 년도를 4자리로 입력하세요? "))
by = int(input("당신이 태어난 년도를 4자리로 입력하세요? "))
age = y - by + 1
print( f"당신의 나이는 {age} 살입니다." )

print( "-" )

print( "2) 600kg 제한의 화물용 엘리베이터. 2 개의 물건에 대한 무게를 실수로 입력받아 현재 엘베에 더 적재할 수 있는 무게를 구하시오" )
kg1 = float(input("첫 번째 물건의 무게를 입력하시오? "))
kg2 = float(input("두 번째 물건의 무게를 입력하시오? "))
w = 600 - (kg1 + kg2)
print( f"현재 엘리베이터의 허용 무게는 {w} kg입니다" )


print( "-" * 100 )


#Q4.
print( "#Q4." )
print( "1) 키를 입력하여 표준 체중 구하기" )
# 표준 체중 = (현재 키 - 100) x 0.9
h = float(input("키를 입력하세요? "))
ew = (h - 100) * 0.9
print( f"표준 체중은 {ew}입니다." )

print( "-" )

print( "2) 현재 체중을 입력하고 1 번에서 구한 표준 체중을 이용하여 비만도 구하기" )
# 비만도(%) = (현재 체중 / 표준 체중) x 100
w = float(input("현재 체중을 입력하세요? "))
b = ( w / ew ) * 100
print( f"표준 체중은 {ew}이고 비만도는 {round(b,2)}입니다." )


print( "-" * 100 )


#Q5.
print( "#Q5. 학생 이름과 국어, 영어, 수학 점수를 입력받아 출력하시오" )
name = input("학생 이름: ")
kor = int(input("국어 점수: "))
eng = int(input("영어 점수: "))
mat = int(input("수학 점수: "))
sum_ = kor + eng + mat
avr_ = round(sum / 3, 2)
print( "=" * 20,"학생 정보","=" * 20 )
print( "이름\t국어\t영어\t수학\t합계\t평균")
print( "-" * 51 ) 
print( f"{name}\t{kor}\t{eng}\t{mat}\t{sum_}\t{avr_}")


