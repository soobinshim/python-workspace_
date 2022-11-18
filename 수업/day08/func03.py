'''
def showAvrt(a,b,c):
    print( f"{a}와 {b}의 평균: {round(c,1)}" )

def avrg(j, k):
    return (j+k) / 2

def display():
    i = 2
    j = 3
    f = avrg(i, j)
    showAvrt(i, j, f)
display()
print( "다음 문장 실행" )
'''


print( "-" * 100 )


def Check_value(li, num):
    for i in li:
        if num == i:
            return 1
    return 0

year = [ '1999' , '2000' , '2001' ]
num = input('저장할 년도 입력 : ' )

check = Check_value( year, num )

if check == 1:
    print( '해당 년도는 존재 합니다. 저장할 수 없음!!!' )
else:
    year.append( num )
    print( num , ' 저장 되었습니다!!!' )
    

menu = [ '라면' , '순대' , '김밥' ]
num = input('등록 메뉴 입력 : ' )

check = Check_value(menu, num)

if check == 1:
    print( '해당 메뉴는 존재 합니다. 저장할 수 없음!!!' )
else:
    menu.append( num )
    print( num,' 저장 되었습니다!!!' )







