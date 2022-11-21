'''
상속
- 이미 만들어진 코드를 상속받는 것
- 상속받으면 상속받은 코드를 사용할 수 있다.
'''
'''
class Calc:
    def calc(self):
        print( "부모 나는 계산기" )

#c = Calc()
#c.calc()

class Computer(Calc):   # 괄호 안에 상속받고자 하는 클래스 이름을 넣는다
    def calc(self):
        print( "자식 나는 계산기" )
    
    def computer(self):
        print( "나는 컴퓨터" )
        self.calc() # 부모 클래스와 같은 값일 때, 자기 자신이 우선
        super().calc()    # 부모 클래스의 값이 우선

c = Computer()
c.computer()
#c.calc()
'''


'''
class MemberInfo:   # 사용자의 인적 사항 저장 위한 클래스
    def inputMember(self, m):
        while True:
            self.name = input("이름: ")
            if m.get(self.name) != None:
                print( "아이디 있음" )
                continue
            break
        self.age = input("나이: ")
        self.addr = input("주소: ")

class Display:      # 입력받은 값을 보여 주는 클래스   
    def display(self):
        mem_dic = {}
        for i in range(3):
            self.mem = MemberInfo()
            self.mem.inputMember(mem_dic)
            #print( self.mem.name )
            mem_dic[self.mem.name] = self.mem
        print( "--- 내용 출력 ---")
        for k, v in mem_dic.items():
            #print( k,":",v )
            print( v.name )
            print( v.age )
            print( v.addr )
            print( "-------" )
        # print( mem_dic )
        # print( mem_dic[self.mem.name] )
        # print( mem_dic[self.mem.name].name )
        # print( mem_dic[self.mem.name].age )
        # print( mem_dic[self.mem.name].addr )

m = MemberInfo()
d = Display()
d.display()
'''





#Q.
import os

class Computer:
    def __init__(self, version={}, function={}):
        self.version = version
        self.function = function
    
    def printVersion(self):
        print( "사양을 보여 줍니다" )
        print( "------------------" )

        for k, v in self.version.items():
            print( k,":",v )
        print( "------------------" )

    def printFunction(self):
        print( "기능을 보여 줍니다" )
        print( "------------------" )

        for k, v in self.function.items():
            print( k,":",v )
        print( "------------------" )
        
        value = input("사용할 기능 입력: ")
        os.system(self.function[value])
    
    def display(self):
        self.version = {"cpu":"i7", "memory":"8"}
        self.function = {"계산기":"calc", "메모장":"notepad"}

        while True:
            print( "1. version 확인" )
            print( "2. 기능 확인" )
            print( "3. 종료" )
            num = int(input(">>> "))

            if num == 1:
                self.printVersion()
            elif num == 2:
                self.printFunction()
            else:
                break

class Member:
    def inputMember(self, info={}):
        self.name = input("이름 입력: ")
        while True:
            self.id = input("아이디 입력: ")
            if info.get(self.id) != None:
                print( "동일한 아이디가 있습니다. 다시 입력하세요." )
            else:
                break
        self.pw = input("비밀번호 입력: ")   

class Login(Computer):
    def userCheck(self, info, userid, userpw):
        if info.get(userid) != None:
            if info.get(userid).pw == userpw:
                return 0
            else:
                return 1
        return -1

info = {}
login = Login()

while True:
    num = input("1. 로그인  2. 회원가입  3. 모든 사용자 보기  4. 종료\n>>> ")

    if num == '1':
        userid = input("인증할 아이디 입력: ")
        userpw = input("인증할 비밀번호 입력: ")
        result = login.userCheck(info, userid, userpw)

        if result == 0:
            print( "인증 통과" )
            login.display()
        elif result == 1:
            print( "비밀번호 틀림" )
        else:
            print( "존재하지 않는 아이디입니다" )
    elif num == '2':
        mem = Member()
        mem.inputMember(info)
        info[mem.id] = mem
        print( "회원가입을 축하합니다" )
    elif num == '3':
        print( "=== 모든 사용자 보기 ===")
        for k, v in info.items():
            print( "이름:", v.name )
            print( "아이디:", v.id )
            print( "비밀번호:", v.pw )
            print( "-" * 15 )
    elif num == '4':
        print( "종료합니다" )
        break




