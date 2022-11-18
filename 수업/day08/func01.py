'''
함수(메소드)
- class 안에 함수가 있으면 메소드라 호칭
- class 없이 함수만 있으면 함수
- 어떤 기능이 있다면 함수라고 한다
- 소괄호가 존재하면 95% 정도는 함수다
ex. print(); input(); st = ""; st.lower()

사용 방법
def 함수이름(매개변수)
def test(args):
    종속 문장
    return value
'''

def reverseCode():  
    temp = 0
    result = int(input("수 입력: "))
    while True:
        temp = result % 10
        result = result // 10
        print( temp, end=", " )
        if not result:  # if result == 0:
            break
    print( "프로그램 종료" )

if __name__ == "__main__":  # 현재 파일에서만 실행
    print( "main" )
    reverseCode()   # 함수는 호출을 해야 실행이 됨


