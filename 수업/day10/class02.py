'''
class
- 틀. 틀 안에 모든 기능과 변수가 존재한다
- 하나의 자료형이다
객체
- 클래스 자료형으로 변수를 만들면 객체라고 표현한다
메소드
- 클래스 안에 함수를 만들면 메소드라고 한다
'''
'''
class Info:
    name = None
    addr = None
    age = None
    stNum = None
    phNum = None
i = Info()  # class는 자료형이어서 하나의 변수로 만듦 i. 으로 class Info에 접근 가능
i.name = "홍길동"
i.age = 20
i.addr = "산골짜기"

print( i.name, i.age, i.addr )

def test():
    i = Info()
    i.name = "테스트"
    print( i.name )

def test1():
    i = Info()
    i.name = "연습중"
    print( i.name )

test()
test1()
'''



'''
class MyClass:
    name = None
    def test(self):
        print( "test 메소드입니다" )
        print( self )
        print( "-" * 20 )
c = MyClass()
c.test()
print( c )
'''

'''
class MethodTest01:
    def sumFunc(self):
        n1 = int(input("수 입력: "))
        n2 = int(input("수 입력: "))
        s = n1 + n2
        print( "합: ", s )
    
    def myInput(self):
        n1 = int(input("수 입력: "))
        n2 = int(input("수 입력: "))
        return n1, n2

    def sumN(self, n1, n2):
        return n1 + n2
    
    def myPrint(self, *t):
        print( f"{t[0]} + {t[1]} = {t[2]}" )

    
obj = MethodTest01()
#obj.sumFunc()
#tul = obj.myInput()
n1, n2 = obj.myInput()
s = obj.sumN(n1, n2)
obj.myPrint(n1, n2, s)
'''


'''
class Myclass:
    def myInput(self):
        n1 = int(input("수 입력: "))
        n2 = int(input("수 입력: "))
        return n1, n2
    
    def Max_(self, n1, n2):
        min_ = 0
        max_ = 0
        if n1 < n2:
            min_ = n1
            max_ = n2
        else:
            min_ = n2
            max_ = n1
        return max_
    
    def myPrint(self, max_):
        print( f"더 큰 수는 {max_}" )

obj = Myclass()
n1, n2 = obj.myInput()
m = obj.Max_(n1, n2)
obj.myPrint(m)
'''


'''
class Myclass:
    def myInput(self):
        n = int(input("수 입력: "))
        return n

    def Main(self, n):
        if n % 2 == 0:
            return "짝수"
        else:
            return "홀수"

    def MyPrint(self, result):
        print( result )

obj = Myclass()
n = obj.myInput()
m = obj.Main(n)
obj.MyPrint(m)
'''


'''
class Myclass:
    def myInput(self):
        n = int(input("수 입력: "))
        return n

    def Main(self, n):
        if n % 3 == 0:
            return "3의 배수"
        else:
            return "3의 배수 아님"

    def myPrint(self, n):
        print( n )

obj = Myclass()
n = obj.myInput()
m = obj.Main(n)
obj.myPrint( m )    
'''  


'''
class Myclass():
    def myInput(self):
        n = int(input("수 입력: "))
        return n
    
    def Main(self, n):
        for i in range(2, n+1):
            cnt = 0
            for j in range(1, i+1):
                if i % j == 0:
                    cnt += 1
        if cnt == 2:
            return "소수"
        else:
            return "소수 아님"
        
    def myPrint(self, n):
        print( n )

obj = Myclass()
n = obj.myInput()
m = obj.Main(n)
obj.myPrint( m )
'''




class Myclass():
    def myInput(self):
        n = int(input("수 입력: "))
        return n

    def Main(self, n):
        if n < 0:
            return -n
        else:
            return n
    
    def myPrint(self, n):
        print( n )

obj = Myclass()
n = obj.myInput()
m = obj.Main(n)
obj.myPrint( m )
