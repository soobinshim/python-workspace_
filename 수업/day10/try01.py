'''
try:    # 프로그램을 멈추지 않는다. 10/0 등 문제가 생겨 에러가 뜰 때 처리하기 위해 사용
    n1 = int(input("수 입력: "))
    n2 = int(input("수 입력: "))

    s = n1 / n2
    print( "결과: ", s)
except ZeroDivisionError:   # ZeroDivisionError 에러가 발생할 때 아래와 같이 처리하겠다는 것
    print( "문제 발생" )
except ValueError:
    print( "문제 발생" )
print( "다음 문장" )
'''

'''
while True:
    try:
        num = int(input("수 입력(종료 0): "))
    except:     # 어떤 에러인지 명시하지 않으면 모든 값들을 아래와 같이 처리하겠다는 것
        #num = "잘못 입력. 다시..."
        print( "잘못 입력. 다시..." )
        continue
    if num == 0:
        break
    print( "입력한 수: ", num )
print( "다음 문장들 실행" )
'''


'''
try:
    n = int(input("수 입력: "))
    print( "입력한 값: ", n )
except:
    print( "except 실행" )
else:
    print( "else 실행" )
print( "다음 문장 실행" )
'''


'''
try:
    n1 = int(input("수 입력: "))
    n2 = int(input("수 입력: "))
    s = n1 / n2
except:
    print( "except 실행" )
else:
    print( f"{n1} / {n2} = {s}" )
finally:
    print( "finally 실행" )
print( "다음 문장 실행" )
'''

'''
def test():
    file = 0
    try:
        file = open("c/aaa111.txt", "r")
    except:
        print( "파일이 존재하지 않습니다" )
    else:
        print( file.read() )
    finally:
        if file:
            file.close()
    print( "이어서 진행" )

    try:
        n = input("수 입력: ")
        if n == "1":
            return 111
        elif n == "2":
            return 222
    except:
        pass
    finally:
        print( "test 함수 실행" )
        print( "이 코드는 무조건 실행" )
    print( "test 함수 종료" )
re = test()
print( "결과: ", re )
'''


'''
try:
    age = int(input("나이 입력: "))
    #print( "당신의 나이는: ", age-1 )

    if age < 0:
        raise Exception("0000안됨") # 강제로 예외를 발생시키는 문법

except ValueError:
    print( "문자는 입력할 수 없음" )
except Exception as e:
    print( "0 살 아래는 안 됨" )
    print( e )
except:
    print( "문제 발생" )
else:
    print( "당신의 나이는: ", age-1 )
'''


print( "-" * 100 )

'''
#Q1. 
print( "#Q1." )

while True:
    try:
       age = int(input('입력 : '))
       st = str(age)
       if age >= 900101 or len(st) != 6:
           print( '가입 불가' )
       elif age <= 891231:
           print( '가입 가능' )
           break
    except:
        print( '잘못 입력' )



try:
    min = input("주민번호 앞 자리 입력(예 900402) : ")

    if len(min) != 6:
        raise Exception("잘못 입력")
    if not min.isdigit(): #숫자로 구성되어 있냐
        raise Exception("잘못 입력 숫자 입력하세요")
    elif min[0] > '8':
        raise Exception(min)
except Exception as e:
    print( e, "가입불가" )
else:
    print( min, ": 가입가능" )
finally:
    print("프로그램 종료 합니다")
'''

    











