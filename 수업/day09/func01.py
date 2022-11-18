'''
def sum_func(x1,x2,x3=100): #x3=100을 이렇게 선언해서 디폴트를 지정해줄수있음
    re = x1+x2+x3 
    return re
re = sum_func(10,20)
print('합:', re)
re = sum_func(10,20,30)
print('합:', re)
'''
'''
def input01():#메뉴번호고르기
    num = int(input('번호를 입력해주세요 :'))
    return num
def func02(num, tm=240, pay=12000):#시간 * 시급 의 결과값을 반환하는 함수
    if num == 1:
        pass
    elif num ==2:
        tm= int(input('사용자가 일한 시간'))
    elif num ==3:
        pay= int(input('사용자의 시급'))
    else :
        tm= int(input('사용자가 일한 시간'))
        pay= int(input('사용자의 시급'))
    return(tm * pay)
print('1.기본급 2.일한 시간설정 3.시급 설정 4.시간&시급 설정')
num= input01()
print(func02(num, tm=240, pay=12000))
'''

'''
print('1.환승 안함\n2.환승함\n3.장거리')
def func01(x=500,y=0):
    num = int(input('수를 입력:'))
    if num==1:
        pass
    elif num ==2:
        y = int(input('환승수 입력: '))
        x = x*(2)*y
    else :
        x=10000
    return x
print(func01(x=500,y=0))
'''