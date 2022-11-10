# import sys, os
# sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

# import day02.elif05 # import : 해당 파일을 현재 페이지로 불러옴
# print( "현재 페이지" )
'''
import os

#data = 0    
data = None # 데이터 초기화
while True:         # while: 무한 반복. 정지는 ctrl + c
    print( "=" * 30 )
    print( "1. 데이터 입력" )
    print( "2. 데이터 출력" )
    print( "3. 종료" )
    print( "=" * 30 )
    num = int(input(">>> "))
    
    if num == 1:
        data = input( "데이터 입력: " )
    elif num == 2:
        if data == None:
            print( "저장 데이터 없음" )
        else:
            print( f"입력 데이터: {data}" )
        os.system("pause")  # 화면 일시정지
    elif num == 3:
        os._exit(1)     # 강제 종료
    
    os.system("cls")    # 화면 clear


print( "-" * 100 )
'''
import os

name = None
sum_ = None
avr_ = None
while True:
    print( "=" * 40 )
    print( "\t\tM E N U" )
    print( "=" * 40 )
    print( " 1. 학생 이름 입력" )
    print( " 2. 성적 3과목(국,영,수) 입력" )
    print( " 3. 학생 이름 출력" )
    print( " 4. 성적 합계 출력" )
    print( " 5. 성적 평균 출력" )
    print( " 6. 종료" )
    print( "=" * 40 )
    num = int(input(">>> "))

    if num == 1:
        name = input("학생 이름 입력: ")
    elif num == 2:
        kor = int(input("국어 점수 입력: "))
        eng = int(input("영어 점수 입력: "))
        mat = int(input("수학 점수 입력: "))
        sum_ = kor + eng + mat
        avr_ = ( sum_ ) / 3
    elif num == 3:
        print ( f"이름: {name}" )
        os.system("pause")
    elif num == 4:
        print ( f"성적 합계: {sum_}" )
        os.system("pause")
    elif num == 5:
        print ( f"성적 평균: {round(avr_,1)}" )
        os.system("pause")
    elif num == 6:
        print( "종료" )
        os._exit(1) 
    else:
        print( "잘못된 입력입니다" )
        os.system("pause")
    
    os.system("cls")


    
