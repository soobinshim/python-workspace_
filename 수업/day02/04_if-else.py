'''
if 조건식:
    종속 문장
else:
    종속 문장
다음 문장들 실행
'''

n = int(input("수 입력: "))

if n % 2 == 0:
    print( "짝수" )
else:
    print( "홀수" )
print( "다음 문장들 실행" )


print( "-" )


n1 = -13

if n1 > 0:
    print( "0보다 크다" )
    if n1 % 2 == 0:
        print( "양의 짝수입니다" )
    else:
        print( "양의 홀수입니다" )
else:
    print( "음수입니다" )


print( "-" )


n1 = "aaa"
n2 = "aaa"

if n1 == n2:
    print( "같다" )
else:
    print( "다르다" )


print( "-" * 100 )


#Q1.
print( "#Q1. 인증 프로그램" )
save_id = input("저장할 ID 입력: ")
save_pw = input("저장할 PW 입력: ")
print( "인증 프로그램입니다\nID와 PW를 입력하세요" )
user_id = input("ID 입력: ")
user_pw = input("PW 입력: ")

if save_id == user_id:
    if save_pw == user_pw:
        print( "인증 통과!!!" )
    else:
        print( "비밀번호가 틀렸습니다" )
else:
    print( "등록되지 않은 아이디입니다" )








