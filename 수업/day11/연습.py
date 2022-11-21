import os

class Computer:
    def __init__(self , version = {} , function = {} ):
        self.version = version
        self.function = function
    def printVersion(self):
        print( "사양을 보여 줍니다" )
        print("------------------")
        for k, v in self.version.items() :
            print(k,":",v)
        print("------------------")
    def printFunction(self):
        print( "기능을 보여 줍니다" )
        print("------------------")
        for k, v in self.function.items() :
            print(k,":",v)
        print("------------------")
        value = input("사용할 기능 입력 : ")
        os.system(self.function[value])
    def display(self):    
        self.version = {"cpu":'i7' , "memory":'8'}
        self.function = {"계산기":"calc", "메모장":"notepad"}
        while True:
            print("1. version확인")
            print("2. 기능 확인")
            print("3. 종료")
            num = int( input(">>> : ") )
            if num == 1:
                self.printVersion()
            elif num == 2:
                self.printFunction()
            else:
                break
class Member:
    def inputMember(self , info={}):
        self.name = input( "이름 입력 : " )
        while True:
            self.id = input( "아이디 입력 : " )
            if info.get( self.id ) != None:
                print( "동일한 아이디. 다시 입력" )
            else: break
        self.pwd = input( "비밀번호 입력 : " )
class Login( Computer ):
    def userChk(self , info , userId , userPwd ):
        if info.get(userId) != None:
            if info.get(userId).pwd == userPwd:
                return 0
            else: return 1
        return -1

info = {}
login = Login()
while True:
    num = input("1.로그인 2.회원가입 3.모든 사용자 보기 4.종료 >>> :")
    if num == '1':
        userId = input("인증할 아이디 입력 : ")
        userPwd = input("인증할 비밀번호 입력 : ")
        result = login.userChk( info , userId , userPwd)
        if result == 0:
            print( '인증 통과' )
            login.display()
        elif result == 1:
            print( "비밀번호 틀림" )
        else:
            print( "존재하지 않는 아이디 입니다" )
    elif num == '2' :
        mem = Member()
        mem.inputMember( info )
        info[mem.id] = mem
        print( "회원 가입을 축하 합니다" )
    elif num == '3':
        print("=== 모든 사용자 보기 ===")
        for k , v in info.items():
            print("이름 : " , v.name)
            print("아이디 : " , v.id)
            print("비밀번호 : " , v.pwd)
            print( "-" * 15 )
class Computer:
    def __init__(self , version = {} , function = {} ):
        self.version = version
        self.function = function
    def printVersion(self):
        print( "사양을 보여 줍니다" )
        print("------------------")
        for k, v in self.version.items() :
            print(k,":",v)
        print("------------------")
    def printFunction(self):
        print( "기능을 보여 줍니다" )
        print("------------------")
        for k, v in self.function.items() :
            print(k,":",v)
        print("------------------")
        value = input("사용할 기능 입력 : ")
        os.system(self.function[value])
    def display(self):    
        self.version = {"cpu":'i7' , "memory":'8'}
        self.function = {"계산기":"calc", "메모장":"notepad"}
        while True:
            print("1. version확인")
            print("2. 기능 확인")
            print("3. 종료")
            num = int( input(">>> : ") )
            if num == 1:
                self.printVersion()
            elif num == 2:
                self.printFunction()
            else:
                break
