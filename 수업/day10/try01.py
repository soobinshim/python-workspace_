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




try:
    n = int(input("수 입력: "))
    print( "입력한 값: ", n )
except:
    print( "except 실행" )
else:
    print( "else 실행" )
print( "다음 문장 실행" )




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












