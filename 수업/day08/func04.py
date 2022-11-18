'''
지역변수(local variable)
- 특정 지역에서만 사용 가능
전역변수(global variable)
- 코드 전체에서 사용 가능
'''
'''
def func01():
    #global a    # 전역변수로 사용하겠다는 것
    a = 100     # 지역변수
    print( "func01 :", a)
def func02():
    #a = 200    # 지역변수
    print( "func02 :", a)

a = 1234     # 전역변수
func01()
func02()


print( "-" )


def func2(a,b):
    a += 5
    b *= 10
    print( "func2: a={}, b={}".format(a,b) )

def func1():
    a = 5
    b = 10
    func2(a,b)
    print( "func1: a={}, b={}".format(a,b) )

func1()


print( "-" )
'''

def display():
    num = 10
    print( "10까지의 합:", sumFunc(num) )

def sumFunc(num):
    sum_ = 0
    for i in range(num + 1):
        sum_ += i
    return sum_

display()



#전역변수: num, sum_ 만들어서 실행되게 변경

def display():
    sumFunc()
    print( "10까지의 합:", sum_ )

def sumFunc():
    global sum_
    for i in range(num + 1):  
        sum_ += i
    return sum_

num = 10
sum_ = 0
display()