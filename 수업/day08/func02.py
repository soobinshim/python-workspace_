'''
# 강한 결합
def SumFunc():
    sum_ = 0
    num = int(input("수 입력: "))
    for i in range( num+1 ):
        sum_ += i
    print( f"1~{num}까지의 합: {sum_}" )
#SumFunc()


# 약한 결합
def SumFunc1( num ):
    sum_ = 0
    for i in range( num+1 ):
        sum_ += i
    print( f"1~{num}까지의 합: {sum_}" )

#num = int(input("수 입력: "))
#SumFunc1( num )


def SumFunc2( num ):
    sum_ = 0
    for i in range( num+1 ):
        sum_ += i
    return sum_

# num = int(input("수 입력: "))
# sum_ = SumFunc2( num )
# print( f"1~{num}까지의 합: {sum_}" )


# ls = set()
# ls.add(10)
# print( "ls: ", ls )
# result = ls.pop()
# print( result )
# print( "ls: ", ls )


print( "-" * 100 )


# Q1. 연산, 출력, 입력 함수를 각각 만들어 동작
def InputFunc():
    num = int(input("수 입력: "))
    return num

def SumFunc(num):
    sum_ = 0
    for i in range( num + 1 ):
        sum_ += i
    return sum_

def PrintFunc(num, sum_):
    print( f"1~{num}까지의 합: {sum_}" )

num = InputFunc()
sum_ = SumFunc( num )
PrintFunc(num, sum_)


print( "-" * 100 )


# Q2.
def InputFunc():
    num = int(input("수 입력: "))
    return num

def MainFunc(num):
    if num % 3 == 0:
        print( f"{num}은 3의 배수" )
    else:
        print( f"{num}은 3의 배수가 아님" ) 

num = InputFunc()
MainFunc(num)


print( "-" )


def Myinput():
    num = int(input("수 입력: "))
    return num

def test(num):
    if num % 3 == 0:
        result = f"{num}은 3의 배수"
    else:
        result = f"{num}은 3의 배수 아님"
    return result

def Myprint(result):
    print( result )

n = Myinput()
r = test(n)
Myprint(r)



print( "-" * 100 )



def InputFunc():
    num = int(input("수 입력: "))
    return num

def MainFunc(num):
    li = []
    for i in range(1, num+1):
        if num % i == 0:
            li.append(i)

    if len(li) == 2:
        print( f"{num}은 소수" )
    else:
        print( f"{num}은 소수가 아니다" )

num = InputFunc()
MainFunc(num)


print( "-" )


def Myinput():
    num = int(input("수 입력: "))
    return num

def test(num):
    cnt = 0
    for i in range(1, num+1):
        if num % i == 0:
            cnt += 1
    if cnt == 2:
        return f"{num}은 소수"
    return f"{num}은 소수 아님"

def Myprint(result):
    print( result )

n = Myinput()
r = test(n)
Myprint(r)



print( "-" * 100 )



def InputFunc():
    temp = 0
    result = int(input("수 입력: "))
    return temp, result

def reverseCode(temp, result):  
    while True:
        temp = result % 10
        result = result // 10
        print( temp, end="" )

        if not result:  # if result == 0:
            break

temp, result = InputFunc()
reverseCode(temp, result)


print( "-" )



def inputNum():
    num = int(input('수를 입력 :'))
    return num

def rev(num):
    li=[]
    while True:   
        rest_ = num%10 #일의 자리
        li.append(rest_)
        num=num//10
        if num==0:
            break
    return li

li=rev(inputNum())
print(li)



print( "-" * 100 )
'''


# def InputFunc():
#     num1 = int(input("1 입력: "))
#     num2 = int(input("2 입력: "))
#     a = input("연산기호 입력: ")
#     return num1, num2, a

# def MainFunc(num1, num2, a):
#     if a == '+':
#         print( num1 + num2 )
#     elif a == '-':
#         print( num1 - num2 )
#     elif a == '*':
#         print( num1 * num2 )
#     elif a == '/':
#         print( num1 / num2 )
#     else:
#         print( "잘못 입력" )

# num1, num2, a = InputFunc()
# MainFunc(num1, num2, a)


# print( "-" )


# def Myinput():
#     num1 = int(input("수 입력: "))
#     op = input("입력: ")
#     num2 = int(input("수 입력: "))
#     return num1, op, num2

# def calc( num1, op, num2 ):
#     if op == "+":
#         return num1 + num2
#     elif op == "-":
#         return num1 - num2
#     elif op == "*":
#         return num1 * num2
#     elif op == "/":
#         return num1 / num2
#     else: return "잘못 입력!!!"

# def Myprint(result):
#     print( result )

# num1, op, num2 = Myinput()
# result = calc(num1, op, num2)
# Myprint(result)



# def Myinput():
#     num = int(input("입력: "))
#     return num

# def Test(num):
#     for i in range(1, num+1):
#         cnt = 0
#         if num % i == 0:
#             cnt += 1
           
#         if cnt == 0:
#             return "소수"

# num = Myinput()
# print( Test(num) )


def myinput():
    score = int(input("점수 입력: "))
    return score

def test(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    elif score < 60:
        return "F"
    else:
        return "제대로 입력"

score = myinput()
print( test(score) )


def print_reverse(string):
    print( string[::-1] )
print_reverse("python")


 
            
            
        






    







