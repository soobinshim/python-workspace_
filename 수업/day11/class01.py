'''
클래스 변수: 클래스가 실행될 때 생성
 - 프로그램 내에서 접근 가능
인스턴스(객체) 변수: 객체가 생성될 때 생성
 - 객체를 이용해서만 접근 가능
지역 변수: 특정 지역이 실행될 때 생성 
 - 특정 지역에서만 접근 가능
'''
'''
class Variable01:
    def var(self):
        v = 100 # 지역변수. 같은 클래스 내부여도 다른 함수에 값을 전달해 줘야(return) 사용 가능
        print( "var v:", v)
        return v
    
    def var02(self, v):
        print( "20 v:", v )

vv = Variable01()
v = vv.var()
vv.var02(v)
'''




'''
class Var02:
    def var(self):
        self.v = 100    # 인스턴스변수. 클래스 내부에서 사용 가능. return 안 써도 됨
        print( "var:", self.v )
    
    def var02(self):
        print( "20 v:", self.v )

vv = Var02()
vv.var()
vv.var02()
'''




'''
class Student:
    def inputSt(self):
        self.name = input("이름 입력: ")    # 다른 지역에서 공통으로 사용하는 건 인스턴스변수로 사용
        self.age = input("나이 입력: ")
        i = 5          # 해당 지역에서만 사용하는 건 그냥 지역변수로 사용
        while i < 10:
            print()
            i += 1
    
    def printSt(self):
        print( self.name, "님" )
        print( self.age, "살" )

s = Student()
s.inputSt()
s.printSt()
'''






#Q1. 인스턴스 변수 사용한 성적 프로그램
class Student():
    def inputSt(self):
        self.name = input("이름 입력: ")
        self.kor = int(input("국어 입력: "))
        self.eng = int(input("영어 입력: "))
        self.mat = int(input("수학 입력: "))

    def setSum(self):
        self.sum = self.kor + self.eng + self.mat

    def setAvg(self):
        self.avg = round(self.sum / 3, 1)
        
    def setGrade(self):
        if self.avg >= 90:
            self.grade = 'A'
        elif self.avg >= 80:
            self.grade = 'B'
        elif self.avg >= 70:
            self.grade = 'C'
        else:
            self.grade = 'F'

    def printSt(self):
        print("이름 : " , self.name )
        print( f"국: {self.kor}, 영: {self.eng}, 수: {self.mat}" )
        print("합계:" , self.sum )
        print("평균:" , self.avg )
        print("등급:" , self.grade )

        
s = Student()
s.inputSt()
s.setSum()
s.setAvg()
s.setGrade()
s.printSt()
        



