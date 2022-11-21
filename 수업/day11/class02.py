'''
class AAA:
    def test1(self):
        print( "test1:" )
        print( self.num )

a = AAA()
a.num = 12345
a.test1()
'''

'''
class BBB:
    aaa = "안녕안녕"    # 클래스변수. 프로그램 종료 전까지 계속 살아 있음. 다른 함수(지역)에서도 사용 가능
    def test1(self):
        print( "test1:" )
        print( self.aaa )
        print( BBB.aaa )

#b = BBB()
#b.test1()
print( BBB.aaa )    # 클래스변수는 클래스 통해 바로 접근
BBB.num = "넘~" # 클래스변수는 클래스 이름으로 접근
print( BBB.num )

b = BBB()
b.bbb = "bbb입니다" # 인스턴스 변수
#print( BBB.bbb )    # 인스턴스 변수는 클래스로 접근 불가
print( b.bbb )  # 인스턴스 변수는 객체를 이용해서 접근

def test():
    b = BBB()
    b.test1()
test()
'''


'''
class CCC:
    def test(): # self 생략하고 만드는 메서드는 클래스 변수
        print( "test입니다" )
    
    def test1(self):
        print( "self입니다" )

CCC.test()  # 클래스 변수는 객체 생성 없이 바로 클래스로 접근 가능
c = CCC()
c.test1()   # self 사용한 함수는 객체 생성해야 함
'''



'''
생성자
- 객체가 만들어질 때 자동으로 호출되는 메소드
- __init__(self) 이름을 사용한다
- 일반적으로 변수 초기화 목적으로 사용한다
'''
'''
class TestClass:
    def __init__(self):
        print( "생성자 실행" )
    
    def test(self):
        pass

t = TestClass() # 생성자는 객체 만들 때 바로 호출됨
t.test()
'''

'''
class TestClass02:
    def __init__(self, name):
        self.name = name
    
    def printName(self):
        print( "당신의 이름은:", self.name )

n = input("이름 입력: ")
t = TestClass02(n)
t.printName()
'''


'''
class TestClass03:
    def __init__(self, version, memory):
        self.version = version
        self.memory = memory

    # def setVersion(self, version):
    #     self.version = version
    
    def printM(self):
        print( "버전:", self.version )
        print( "메모리:", self.memory )

    def __str__(self):
        #return "원하는 값 표현"
        return f"{self.version}, {self.memory}"

t = TestClass03("win10", "8G")
# t.setVersion("버전 정보")
t.printM()

print( "t:", t )
'''

'''
import os
os.system("calc")
'''



#Q2.
import os
class Computer:
    def __init__(self, version={}, function={} ):
        self.version = version
        self.function = function

    def printVersion(self):
        print( "사양을 보여 줍니다" )
        print( "------------------" )

        for k, v in self.version.items() :
            print( k,":",v )
        print( "------------------" )

    def printFunction(self):
        print( "기능을 보여 줍니다" )
        print( "------------------" )

        for k, v in self.function.items() :
            print( k,":",v )
        print("------------------")

        value = input( "사용할 기능 입력 : " )
        os.system(self.function[value])
        
version = {"cpu":"i7" , "memory":"8"}
function = {"계산기":"calc", "메모장":"notepad"}
com = Computer(version, function)

while True:
    print( "1. version확인" )
    print( "2. 기능 확인" )
    print( "3. 종료" )
    num = int(input(">>> "))

    if num == 1:
        com.printVersion()
    elif num == 2:
        com.printFunction()
    else:
        break








